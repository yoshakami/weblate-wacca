import os
file_lines_fr = {}
file_lines_en = {}
file_lines_ja = {}
file_lines_vanilla = {}
for file in os.listdir("fr_BE"):
    with open(os.path.join("fr_BE", file), 'r') as po:
        file_lines_vanilla[file] = po.readlines() # this contains \n
        
for file in os.listdir("en_US"):
    with open(os.path.join("en_US", file), 'r') as po:
        file_lines_en[file] = po.readlines() # this contains \n
        
for file in os.listdir("jp_JA"):
    with open(os.path.join("jp_JA", file), 'r') as po:
        file_lines_ja[file] = po.readlines() # this contains \n
        
for file in os.listdir("en_US"):
    with open(os.path.join("en_US", file), 'r') as po:
        file_lines_fr[file] = po.readlines() # this contains \n

for file in os.listdir("fr_BE"):
    for i in range(len(file_lines_vanilla)):
        if "msgstr" in file_lines_vanilla[file][i]:
            file_lines_vanilla[file][i] = "msgstr" + file_lines_vanilla[file][i - 1][5:] 
            file_lines_en[file][i] = file_lines_en[file][i - 1]
            file_lines_ja[file][i] = file_lines_ja[file][i - 1]
            file_lines_fr[file][i-1] = "msgstr" + file_lines_vanilla[file][i - 1][5:] 
            file_lines_en[file][i-1] = "msgstr" + file_lines_vanilla[file][i - 1][5:]
            file_lines_ja[file][i-1] = "msgstr" + file_lines_vanilla[file][i - 1][5:]
    with open(os.path.join("fr_BE", file), "w") as po:
        po.write(file_lines_vanilla[file])
    with open(os.path.join("fr_FR", file), "w") as po:
        po.write(file_lines_fr[file])
    with open(os.path.join("en_US", file), "w") as po:
        po.write(file_lines_en[file])
    with open(os.path.join("jp_JA", file), "w") as po:
        po.write(file_lines_ja[file])