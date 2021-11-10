import os
from pathlib import Path

def gen_init_py(dir_path):
    f = open(dir_path+"/__init__.py", "a")
    f.write("create by xuhuaqing.")
    f.close()

for x in range(1, 17):
    dir_path = f"chapter_{x}"
    if Path(dir_path).is_dir():
        gen_init_py(dir_path)
    else:
        os.mkdir(dir_path)
        gen_init_py(dir_path)