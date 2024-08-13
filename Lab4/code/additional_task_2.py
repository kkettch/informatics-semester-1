import re
import time

yaml = open("schedule_tuesday.yaml", "r") #открытие yaml-файла для записи (r)
xml = open("schedule_tuesday.xml", "w") #открытие xml-файла для чтения (w)
xml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
indent = '  '
mas = []
nes = []
flag = False

start_time = time.time()

for line in yaml:
    reg = re.split(r':', line, maxsplit=1)
    nesting = line.count(indent)
    ex = re.findall(r'[\S]', reg[0])[0]

    if ex == "-":
        nesting += 1
        part = "".join(re.findall(r"\w+", reg[0]))

    if ex == "-" and flag == True:
        xml.write((indent*(len(mas)-1)) + "</" + mas[-1] + ">" + "\n")

    if nesting not in nes:
        nes.append(nesting)
        nes.sort()
    elif nesting < nes[-1] and ex != '-':
        for i in range(nes[-1] - nesting):
            xml.write((indent * (len(mas)-1)) + "</" + mas[-1] + ">" + "\n")
            del mas[-1]
            del nes[-1]

    if reg[1] != "\n":
        first_part = "".join(re.findall(r"[-\S]+\w", reg[0]))
        second_part = "".join(re.findall(r"'([^']*)'", reg[1]))
        xml.write((indent * nesting) + "<" + first_part + ">" + second_part + "</" + first_part + ">" + '\n')
    else:
        part = "".join(re.findall(r"\w+", reg[0]))
        xml.write((indent * nesting) + "<" + part + ">" + "\n")
        if flag == True and ex == "-":
            del mas[-1]
        mas.append(part)

    if ex == "-" and flag == False:
        flag = True

if mas != []:
    for i in range(len(mas)):
        xml.write((indent * (len(mas)-1)) + "</" + mas[-1] + ">" + "\n")
        del mas[-1]

print((time.time() - start_time) * 100)