from pyipip import IPIPDatabase
f=open('cnip.txt')
fout=open('ipoutput.txt','w')
db = IPIPDatabase('17monipdb.dat')
for line in f:
    ip=str.strip(line)+'   '+db.lookup(str.strip(line))
    print(ip)
    fout.write(ip+'\n')

f.close()
fout.close()


