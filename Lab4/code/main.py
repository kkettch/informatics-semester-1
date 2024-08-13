import time

yaml = open("schedule_tuesday.yaml", "r") #открытие yaml-файла для записи (r)
xml = open("schedule_tuesday.xml", "w") #открытие xml-файла для чтения (w)
xml.write('<?xml version="1.0" encoding="UTF-8"?>\n') #заполняем XML пролог в xml-файл и добавляем переход на следующую строку
indent = '  '
mas = []
nes = []
flag = False

start_time = time.time()

for line in yaml:
    a = line.split(": ", 1)
    nesting = line.count(indent)
    ex = a[0].lstrip()[0]
    if ex == "-":
        nesting += 1
        a[0] = a[0].lstrip()
        a[0] = a[0][2: ]

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

    if len(a) == 1:
        xml.write((indent*nesting) + "<" + a[0][: -2].lstrip() + ">" + "\n")
        if flag == True and ex == "-":
            del mas[-1]
        mas.append(a[0][: -2].lstrip())

    if len(a) == 2:
        a[1] = a[1][1: -2]
        a[0] = a[0].lstrip()

        xml.write((indent * nesting) + "<" + a[0] + ">" + a[1] + "</" + a[0] + ">" + '\n')

    if ex == "-" and flag == False:
        flag = True

if mas != []:
    for i in range(len(mas)):
        xml.write((indent * (len(mas)-1)) + "</" + mas[-1] + ">" + "\n")
        del mas[-1]

print((time.time()-start_time) * 100)