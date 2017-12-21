import re
fin = open('input.txt','r')
fout = open('output.txt','w')
fmold = open('mold.txt','r')
StrPatten = r'(\w+)'
paraNum = len(fin.readline().split())
for i in range(paraNum-1):
    StrPatten += r'\W+(\w+)'
fin.seek(0)
p = re.compile(StrPatten)
mold = fmold.read()
for line in fin:
    replceStr = p.sub(mold, line)
    fout.write(replceStr)
fin.close(), fout.close(), fmold.close()
