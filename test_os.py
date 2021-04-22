import os
import requests

link = ["23.10-задача.py", "dom.py"]

for i in ["Krumaka"]:
    try:
        os.mkdir(i)
    except FileExistsError:
        pass

os.chdir("Krumaka")

for j in link:
    r = requests.get("https://raw.githubusercontent.com/Krumomir/Python-TUES/main/" + j)
    with open(j, "wb") as f:
        for i in r.iter_content(chunk_size=8192):
            f.write(i)