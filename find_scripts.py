import sys

def readme():
    print("[*] find_scripts.py")
    print("Attempts to find scripts inside of an html-based file. Could also be .txt file containing html info")
    print("args: |html|")
    print("Author: Magnus Langhelle" + "\n")

def get_scripts(html):
    printstring = ""
    for elem in html.split('<script src="'):
        currentScript = ""
        for char in elem:
            if char == '"':
                break
            currentScript += char
        if "." in currentScript:
            printstring += currentScript.strip() + "\n"
    return printstring

if __name__ == '__main__':
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        content = f.read()
    print(get_scripts(content))