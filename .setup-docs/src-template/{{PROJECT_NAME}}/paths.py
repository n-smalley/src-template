from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# Enter Paths here

MAX_PATH_LEN = 260
check = {
    k:v 
    for k,v in globals().items() 
    if not k.startswith('_') and k != 'Path' and isinstance(v,Path)
}

for var_name,var_path in check.items():
    str_path = str(var_path)
    if len(str_path) >= MAX_PATH_LEN:
        raise ValueError(
            f"{var_name} length={len(str_path)} exceeds {MAX_PATH_LEN}:\n{str_path}"
        )