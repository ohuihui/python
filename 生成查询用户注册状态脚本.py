import os

f = os.listdir()
f = [name for name in f if name[0:5] == 'ALLME']
f.sort(reverse=True)

SrcFile = open(f[0], 'r')
DesFile = open('查询注册用户脚本.txt', 'w')
DesFile.write('USE ME:MEID=281;\n')
for line in SrcFile:
    if line.startswith('ADD ASBR'):
        IMPU = line[line.index('PUI="') + 5:line.index('",PRI=')]
        DesFile.write(r'DSP USR: QT=IMPU, IMPU="{}";'.format(IMPU))
        DesFile.write('\n')

SrcFile.close()
DesFile.close()
print('Job is done')
