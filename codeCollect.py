import re
from glob import glob
from pathlib import Path

# ----------------
# Config

# Output filename
output_filename = "xyz.txt"

# Masks for filenames to exclude
exc = [
    "codescrapper.py",
    # for example:
    "__pycache__",
    "venv",
    ".idea"
]

# divider pattern (between files)
t1 = "\n" + "_" * 50 + "\n"
t2 = "\n" + "‾" * 50 + "\n"
# ----------------

chk_pat = '(?:{})'.format('|'.join(exc))

file_contents = []

for filename in glob('**/*', recursive=True):
    if bool(re.search(chk_pat, str(filename), flags=re.I)):
        print('Skip ', str(filename))
    elif Path(filename).is_dir():
        pass
    else:
        try:
            with open(filename, encoding='utf-8') as python_file:
                file_contents.append(t1 + python_file.name + t2)
                file_contents.append(python_file.read())
        except Exception as e:
            print(filename, e)

project_code = ''.join(file_contents)
f = open(output_filename, 'w', encoding='utf-8')
try:
    f.write(project_code)
finally:
    f.close()
