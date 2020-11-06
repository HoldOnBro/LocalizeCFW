from shutil import copyfile

dic = {}
copyfile('original_rend.js', 'temp_rend.js')
with open('dic4rend.txt',encoding='utf-8') as d:
    for line in d:
        (key, val) = line.strip('\n').split('\t')
        dic[key] = val

list = []
with open('dic4rend.txt', 'r',encoding='utf-8') as f:
    for line in f:
        list.append(line.strip())
with open("dic4rend.txt", "w",encoding='utf-8') as f:
    for item in sorted(list):
        f.writelines(item)
        f.writelines('\n')

with open("temp_rend.js",encoding='utf-8') as r:
    newText = r.read()
    for key in dic.keys():
        newText = newText.replace(key, dic[key])
with open("renderer.js", "w",encoding='utf-8') as f:
    f.write(newText)

dicMain = {}
copyfile('original_main.js', 'temp_main.js')
with open('dic4main.txt',encoding='utf-8') as md:
    for line in md:
        (key, val) = line.strip('\n').split('\t')
        dicMain[key] = val
with open("temp_main.js",encoding='utf-8') as mr:
    newText = mr.read()
    for key in dicMain.keys():
        newText = newText.replace(key, dicMain[key])
with open("main.js", "w",encoding='utf-8') as mf:
    mf.write(newText)