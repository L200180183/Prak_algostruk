import re

f = open('indonesia.txt', 'r', encoding='latin1')
teks = f.read()
f.close()

#No1
p = r'\s(me\w+)'
nomor1 = re.findall(p, teks)

#No2
p = r'\s(di\w+)'
nomor2 = re.findall(p, teks)

#No3
p = r'\s(di\s\w+)'
nomor3 = re.findall(p, teks)

g = open('KEI.html', 'r', encoding='latin1')
teks = g.read()
g.close()
#No4
i = r'\s<td>[\d\.\w\/]+</td>'
p = r'(\w+)</a></td>' + i + i + i + r'\s<td>([\d\.\w\/]+)</td>'
cocok = re.findall(p, teks)
nomor4 = [(i[0], float(i[1])) for i in cocok]

#FAKHAR SWASTIKA AL-BAIHAQI (L200180183)
