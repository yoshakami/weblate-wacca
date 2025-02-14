import os
for file in os.listdir('fr_FR'):
    with open('fr_FR/' + file, 'r', encoding="utf-8") as po:
        lines = po.readlines()
    out = ""
    for line in lines:
        if "msgstr" in line:
            out += 'msgstr ""\n'
        else:
            out += line
    with open('fr_FR/' + file, 'w', encoding="utf-8") as po:
        po.write(out)
    