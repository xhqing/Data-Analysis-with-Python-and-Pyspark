import os
from pathlib import Path

def gen_init_py(dir_path):
    f = open(dir_path+"/__init__.py", "w")
    f.write("Created by xuhuaqing.")
    f.close()

if __name__=="__main__":
    chap_num = ["0"+str(x) for x in range(1,10)] + [str(x) for x in range(10, 17)]
    for x in chap_num:
        dir_path = f"chapter_{x}"
        if Path(dir_path).is_dir():
            gen_init_py(dir_path)
        else:
            os.mkdir(dir_path)
            gen_init_py(dir_path)