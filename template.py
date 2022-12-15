import os

dir = [os.path.join("data","raw"),
os.path.join("data","processed"),
"src",
"notebook",
"saved_files"]

for dir_ in dir:
    os.makedirs(dir_,exist_ok=True)
    with open(os.path.join(dir_,".gitkeep"),"w") as f:
        pass

files=["params.yaml",
"dvc.yaml",
".gitignore",
os.path.join("src","__init__.py")]

for file_ in files:
    with open(file_,"w") as f:
        pass