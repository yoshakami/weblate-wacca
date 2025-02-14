import os
file_lines_fr = {}
file_lines_en = {}
file_lines_ja = {}
file_lines_vanilla = {}
for file in os.listdir("fr_BE"):
    with open(os.path.join("fr_BE", file), 'r', encoding="utf-8") as po:
        file_lines_vanilla[file] = po.readlines() # this contains \n
        
for file in os.listdir("en_US"):
    with open(os.path.join("en_US", file), 'r', encoding="utf-8") as po:
        file_lines_en[file] = po.readlines() # this contains \n
        
for file in os.listdir("jp_JA"):
    with open(os.path.join("jp_JA", file), 'r', encoding="utf-8") as po:
        file_lines_ja[file] = po.readlines() # this contains \n
        
for file in os.listdir("en_US"):
    with open(os.path.join("en_US", file), 'r', encoding="utf-8") as po:
        file_lines_fr[file] = po.readlines() # this contains \n

for file in os.listdir("fr_BE"):
    lines_id = []
    file_lines_fr[file][2] = '"Language: fr_FR\\n\n"'
    for i in range(2, len(file_lines_vanilla[file])):
        if "msgstr" in file_lines_vanilla[file][i]:
            print(i, file)
            end = ''
            end_id = 0
            if file_lines_ja[file][i - 1][-1:] == '.' and file_lines_vanilla[file][i - 1][-1:] != '.':
                end = '.'
            if file_lines_vanilla[file][i - 1][-1:] == '.' and file_lines_ja[file][i - 1][-1:] != '.':
                end_id = -1
            if file_lines_vanilla[file][i - 1][:end_id] + end in lines_id: 
                print(file_lines_vanilla[file][i - 1][:end_id])
                file_lines_en[file][i] = ""
                file_lines_ja[file][i] = ""
                file_lines_fr[file][i] = ""
                file_lines_vanilla[file][i] = ""
                file_lines_fr[file][i-1] = ""
                file_lines_en[file][i-1] = "" 
                file_lines_ja[file][i-1] = ""
                file_lines_vanilla[file][i-1] = ""
                continue
            print('writing line')
            lines_id.append(file_lines_vanilla[file][i - 1][:end_id] + end)
            file_lines_en[file][i] = "msgstr" + file_lines_en[file][i - 1][5:end_id] + end
            file_lines_ja[file][i] = "msgstr" + file_lines_ja[file][i - 1][5:end_id] + end
            file_lines_fr[file][i] = 'msgstr ""'
            file_lines_vanilla[file][i] = "msgstr" + file_lines_vanilla[file][i - 1][5:end_id] + end
            file_lines_fr[file][i-1] = "\n" + file_lines_vanilla[file][i - 1][:end_id] + end
            file_lines_en[file][i-1] = "\n" + file_lines_vanilla[file][i - 1][:end_id] + end
            file_lines_ja[file][i-1] = "\n" + file_lines_vanilla[file][i - 1][:end_id] + end
            file_lines_vanilla[file][i-1] = "\n" + file_lines_vanilla[file][i - 1][:end_id] + end
    with open(os.path.join("fr_BE", file), "w", encoding="utf-8") as po:
        po.write(''.join(file_lines_vanilla[file]))
    with open(os.path.join("fr_FR", file), "w", encoding="utf-8") as po:
        po.write(''.join(file_lines_fr[file]))
    with open(os.path.join("en_US", file), "w", encoding="utf-8") as po:
        po.write(''.join(file_lines_en[file]))
    with open(os.path.join("jp_JA", file), "w", encoding="utf-8") as po:
        po.write(''.join(file_lines_ja[file]))