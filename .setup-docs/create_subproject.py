import sys
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLACEHOLDER = '{{PROJECT_NAME}}'
TEXT_EXTENSIONS = {'.py', '.md', '.txt', '.toml', '.bat'}
TEMPLATE_SUBDIR = ROOT / '.setup-docs' / 'src-template' / PLACEHOLDER
DEST_SRC = ROOT / 'src'
SCRIPT_DEST = ROOT / 'scripts'

def validate_project_name(dest_project:Path) -> None:
    project_name = dest_project.name
    parent = dest_project.parent
    if '-' in project_name:
        raise ValueError(f'Invalid character "-" in project_name {project_name}')
    if dest_project.exists():
        raise FileExistsError(f'Subproject named "{project_name}" already exists')
    if project_name.startswith('run_'):
        raise NameError(f'Invalid project name "{project_name}" - project names cannot start with "run_"')
    if (project_name == 'core' and (parent / 'common').exists()) or (project_name == 'common' and (parent / 'core').exists()):
        raise FileExistsError('Only one of "core" or "common" may exist')
    
    
def _create_core_folder(dest_project:Path) -> None:
    dest_dir = DEST_SRC / dest_project.name
    dest_dir.mkdir(parents=True,exist_ok=True)

    copy_files = {
        TEMPLATE_SUBDIR / 'paths.py':dest_dir / 'paths.py',
        TEMPLATE_SUBDIR / 'config.py':dest_dir / 'config.py',
    }
    for src,dest in copy_files.items():
        shutil.copy(src,dest)
    
def _create_subproject(dest_project: Path) -> None:
    shutil.copytree(TEMPLATE_SUBDIR,dest_project)

    for path in dest_project.rglob("*"):
        if path.is_file() and path.suffix in TEXT_EXTENSIONS:
            text = path.read_text(encoding="utf-8")
            path.write_text(
                text.replace(PLACEHOLDER, dest_project.name),
                encoding="utf-8",
            )

    for root, dirs, files in dest_project.walk(top_down=False):
        for d in dirs:
            if PLACEHOLDER in d:
                src = root / d
                src.rename(root / d.replace(PLACEHOLDER, dest_project.name))

        for f in files:
            if PLACEHOLDER in f:
                src = root / f
                src.rename(root / f.replace(PLACEHOLDER, dest_project.name))

    script_dest = Path(SCRIPT_DEST)
    script_dest.mkdir(parents=True, exist_ok=True)

    for path in dest_project.iterdir():
        if path.is_file() and path.name.startswith("run_"):
            path.rename(script_dest / path.name)

def main():
    if len(sys.argv) != 2:
        print('Invalid argument, usage: python .setup-docs/create_subproject.py <subproject_name>')
        sys.exit(1)
    
    project_name = sys.argv[1]

    if not TEMPLATE_SUBDIR.exists():
        raise FileNotFoundError(f'Template package not found at {TEMPLATE_SUBDIR}')
    
    dest_project = DEST_SRC / project_name
    validate_project_name(dest_project)

    if project_name in ['core','common']:
        _create_core_folder(dest_project)
    else:
        _create_subproject(dest_project)
    
    print(f'>> Project "{project_name}" created at {dest_project}')

if __name__ == '__main__':
    main()