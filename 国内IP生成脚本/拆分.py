
finput=open('cnip.txt','r')
fout=open('拆分cnip.txt','w')

for index,line in enumerate(finput):
    if index%250 ==0:
        fout.write('ip address-set cnip{} type object\n'.format(index//250))
    fout.write(line)
finput.close()
fout.close()
