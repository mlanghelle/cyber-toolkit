import sys
import subprocess
from pathlib import Path

from find_scripts import get_scripts

def readme():
    print("[*] dwnld_scripts.py")
    print("Attempts to download all scripts from a certain html based website.")
    print("args: |url|")
    print("Author: Magnus Langhelle" + "\n")

def format(p):
    format = run(['npx', 'prettier', '--write', p])

def run(command):
    print(f"Running.. {" ".join(command)}"+ "\n")
    return subprocess.run(command, capture_output=True, text=True)

def main(url):
    result = run(['curl', url, '-o', 'index.html'])
    if result.returncode != 0:
        print("Error curling :(")
        return


    with open("index.html", "r", encoding="utf-8") as file:
        scripts = get_scripts(file.read())

    print("[*] Curled :)" + "\n")
    format('index.html')

    print("Scripts found: " + "\n" + scripts)

    folder = Path("dwnload")
    if not Path.exists(folder):
        folder.mkdir(parents=True, exist_ok=True)

    for script in scripts.split("\n")[1:]:
        if "." not in script:
            continue
        try:
            name = script.split("/")[-1]
            dwnld_path = url+script
            output = "dwnload/" + name
            download = run(['curl', dwnld_path, '-o', output])
            format(output)
        except Exception:
            print(f"Could not handle {script} for some reason..")
            continue

if __name__ == '__main__':
    main(sys.argv[1])