import sys
import shutil
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parents[1]
PLACEHOLDER = '{{PROJECT_NAME}}'
TEXT_EXTENSIONS = {'.py', '.md', '.txt', '.toml', '.bat'}
TEMPLATE_SUBDIR = ROOT / '.setup-docs' / 'src-template' / PLACEHOLDER
DEST_SRC = ROOT / 'src'
SCRIPT_DEST = ROOT / 'scripts'

def validate_project_name(dest_project:Path) -> None:
    _,project_name = os.path.split(str(dest_project))
    if dest_project.exists():
        raise FileExistsError(f'Subproject named "{project_name}" already exists')
    if project_name.startswith('run_'):
        raise NameError(f'Invalid project name "{project_name}" - project names cannot start with "run_"')
    if '-' in project_name:
        raise ValueError(f'Invalid character "-" in project_name {project_name}')

def main():
    if len(sys.argv) != 2:
        print('Invalid argument, usage: python .setup-docs/create_subproject.py <subproject_name>')
        sys.exit(1)
    
    project_name = sys.argv[1]

    if not TEMPLATE_SUBDIR.exists():
        raise FileNotFoundError(f'Template package not found at {TEMPLATE_SUBDIR}')
    
    dest_project = DEST_SRC / project_name
    validate_project_name(dest_project)
    shutil.copytree(TEMPLATE_SUBDIR,dest_project)

    for path in dest_project.rglob('*'):
        if path.is_file() and path.suffix in TEXT_EXTENSIONS:
            text = path.read_text(encoding='utf-8')
            text = text.replace(PLACEHOLDER,project_name)
            path.write_text(text,encoding='utf-8')

    for root,dirs,files in os.walk(dest_project):
        if PLACEHOLDER in root:
            root.replace(PLACEHOLDER,project_name)
        for dir in dirs:
            if PLACEHOLDER in dir:
                src = os.path.join(root,dir)
                dest = os.path.join(root,dir.replace(PLACEHOLDER,project_name))
                os.rename(src,dest)
        for file in files:
            if PLACEHOLDER in file:
                src = os.path.join(root,file)
                dest = os.path.join(root,file.replace(PLACEHOLDER,project_name))
                os.rename(src,dest)
    
    os.makedirs(SCRIPT_DEST,exist_ok=True)
    for file in os.scandir(dest_project):
        if file.name.startswith('run_'):
            dest = os.path.join(SCRIPT_DEST,file.name)
            os.rename(file.path,dest)

    
    print(f'>> Project "{project_name}" created at {dest_project}')

if __name__ == '__main__':
    main()