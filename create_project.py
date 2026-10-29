from pathlib import Path as path

# current working directory

root=path(".")

# Folders to create

folders=[
"app/api",
"app/core",
"app/rag",
"app/services",
"data",
"templates",
"static",
"uploads",
"tests",

]

# files to create

files=[
    "app/main.py",
    "requirements.txt",
    "ingest_sample_kb.py",
    "run.py",
    ".env",
    "requirements.txt",

]

# create folders
for folder in folders:
    (root/folder).mkdir(parents=True, exist_ok=True)

# create files
for file in files:
    (root/file).touch(exist_ok=True)


print("Project structure created successfully.")