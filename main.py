import re
import urllib.request
#regex = "<(“[^”]*”|'[^’]*’|[^'”>])*>"
regex0 = '(?<=[^<>][^\n])<[^<>]+>(?=\n)'
regex = '<[^<>]+>\n|<[^<>]+>'
def get_text():
    text = ''
    case = int(input('Файл(0),Ссылка(1) или Ссылка в Файле(2): '))
    if case == 0:
        inpt = str(input('Введите название файла: '))
        with open(inpt, encoding="utf-8") as inf:
            for line in inf:
                line = line.strip()
                text += line + '\n'
    elif case == 1:
        inpt = str(input('Введите ссылку: '))
        with urllib.request.urlopen(inpt) as webpage:
            for line in webpage:
                line = line.strip()
                line = line.decode('utf-8')
                text += line + '\n'
    elif case == 2:
        inpt = str(input('Введите название файла: '))
        inf = open(inpt)
        link = inf.readline()
        with urllib.request.urlopen(link) as webpage:
            for line in webpage:
                line = line.strip()
                line = line.decode('utf-8')
                text += line + '\n'
    return text

def processing(text):
    teg = []
    tegs_found = []
    new_text = text
    for m in re.finditer(regex, text):
        teg.append(m.start())
        teg.append(m.end())
        tegs_found.append(teg.copy())
        teg.clear()
    #print(text)
    #print(tegs_found)
    #print(repr(text))
    for i in range(len(tegs_found) - 1, -1, -1):
        t = tegs_found[i - 1][1]  # 'l><he'
        #print(text.find('\n',i - 1, i),i,text[tegs_found[i - 1][1]:tegs_found[i][0]])
        if tegs_found[i - 1][1] != tegs_found[i][0] and i - 1 != -1 and text.find('\n',i - 1, i) == -1:
             new_text = new_text[:t] + ' ' + new_text[t:]
    new_text = re.sub(regex0, '', new_text, count=0)
    new_text = re.sub(regex, '', new_text, count=0)
    return new_text

def save_answer(text):
    fout = open('answer.txt', 'w')
    print(text, file=fout )
    print(processing(text),file=fout)
    fout.close()

text = get_text()
save_answer(text)
print(processing(text))
#input()