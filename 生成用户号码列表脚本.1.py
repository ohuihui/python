import os

f=os.listdir()
f=[name for name in f if name[0:5]=='ALLME']
f.sort(reverse=True)
i=0
SrcFile=open(f[0],'r')
DesFile=open('用户列表.txt','w')
DesFile.write('USE ME:MEID=281;\n')
for line in SrcFile:
    if line.startswith('ADD ASBR'):
        IMPU=line[line.index('+'):line.index('@')]
        DesFile.write(r'{}'.format(IMPU))
        DesFile.write('\n')
        print(i)
        i+=1

SrcFile.close()
DesFile.close()
print('Job is done')