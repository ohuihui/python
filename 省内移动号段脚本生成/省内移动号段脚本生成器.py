#省内移动号段制作脚本生成器 Codeby：李佐辉

def convert2Enum (x): #生成ENUM e164格式
    x=x[::-1]
    y=list(x)
    return '.'.join(y)

def expandnum(pfxinfs): #扩展号段至7位,传入列表，返回所有扩展后的号段
    newlines=[]
    for pfxinf in pfxinfs:
        if len(pfxinf[0])>=7 :
            newlines.append(pfxinf)
        else :
            newlines=newlines+expand(pfxinf)
    return newlines

def expand(x): #递归函数，递归至7位号段
    y=[]
    for i in range(0,10):
        if len(x[0]) < 6:
            y=y+expand([x[0]+str(i),x[1]])
        else :
            y.append([x[0]+str(i),x[1]])
    return y
        





fin = open('input.txt','r')
fout = open('output.txt','w')
lines=fin.readlines()
print('共有号段%s个'% len(lines))
print('共有号段%s个\n'% len(lines),file=fout)

lines=[line.rstrip().split(' ') for line in lines]

codeinf={ '571': ['0','1','HZD'], 
          '572': ['1','2','HUZD'], 
          '573': ['2','3','JXID'], 
          '574': ['3','4','NBOD'], 
          '575': ['4','5','SHXD'], 
          '576': ['5','6','TZHD'], 
          '577': ['6','7','WZHD'], 
          '578': ['7','8','LSHD'], 
          '579': ['8','9','JIHD'], 
          '570': ['9','10','QUZD'], 
          '580': ['10','11','ZSHD']}
lines.sort(key=lambda line:int(codeinf[line[1]][0]))


fout.write('-'*40+'固网ATS脚本'+'-'*40+'\n\n')
fout.write('USE ME:MEID=51;\n\n')

for line in lines :
    fout.write('''ADD CNACLD:LOCNUM={0},URISCH=TEL_URI,PFXCDE=K'{1},CSTP=BASE,CSA=LC,CUSTA=NULL,MINL=4,MAXL=32,TOLLPF=FALSE,RDT=0,ANTIP=0,SPCHG=FALSE,SPCDAF=FALSE,CLPRICHK=FALSE,PQRL=2,OWNEX=FALSE,PRKEX=FALSE,EMCF=FALSE,UNIFTYPE=UNIFORM_WITHNO_SEP,BILUNIFTYPE=UNIFORM_WITHNO_SEP,SENDTYPE=Unsupport_overlap,CHSC=65535,PREPFLG=YES,RM=FPCTRL,CPSOR=NOR,CNATTR=NONE,SAF=NO,CDAI=65535,SSA=INPF_CallTrigger-0&INPF_CallRestrict-0&RetrieveVM-0,ACSP=255,DEST=65535,SNS=NO,PEMC=DEFAULT,AOCO=NO,RESERVED=0,RESERVED1=0;\n'''.format(codeinf[line[1]][0],line[0]  ))


fout.write('\n'*3+'-'*40+'VoLTE_MGCF脚本'+'-'*40+'\n\n')
fout.write('USE ME:MEID=5;\n\n')

for line in lines :
    fout.write('''ADD CNACLD:P=100,PFX=K'{1},ADDR=ALL,CSTP=BASE,CSA=LC,RSNAME="{0}",MINL=11,MAXL=11,ICLDTYPE=UN,DEST=65535,IAC=NO,GAIN=LGN,RDT=0,SNO=0,DP=0,DT=0,RCM=NOC,ECOS=FALSE,TOLLDNLEN=0,SRP=FALSE,NPRTIND=FALSE,ISEACM=FALSE,EACM=0,ISERVICECHECKNAME="INVALID",SPDNCHG=NO,DNPREPARE=FALSE,CLIANA=FALSE,ADDSIG=FALSE,NUMNAME="INVALID",CUGSSNT=NIND,TARIFF=NI,CHGNAME="INVALID",NCN="INVALID",SDCSN="INVALID",SN="LOCAL",MOG="PUBLIC";\n'''.format(codeinf[line[1]][2],line[0]  ))



fout.write('\n'*3+'-'*40+'VoLTE_SCSCF脚本(仅融合关口局地区需要制作)'+'-'*40+'\n\n')
fout.write('USE ME:MEID=5;\n\n')

for line in lines :
    fout.write('''ADD SNRTANA:NRTANATYPE=GLOBAL_NUMBER_PREFIX,NRTANACONT=K'86{1},RTSN="{0}";\n'''.format(codeinf[line[1]][2],line[0]  ))



fout.write('\n'*3+'-'*40+'ENUM脚本'+'-'*40+'\n\n')
fout.write('USE ME:MENAME=ENUM1;\n\n')

expandlines=expandnum(lines)
for line in expandlines :
    fout.write('''ADD_DZONE: ZONENAME="{0}.6.8.e164.arpa", NAPTRPERMIT=TRUE, SRVPERMIT=FALSE, DNSPERMIT=FALSE, NUMLEN=4, TTL=60, MNAME="enumserver.", RNAME="enumserver@huawei.com.", REFRESH=600, RETRY=60, EXPIRE=157680000, ZTYPE=LOCAL_ZONE;\n'''.format(convert2Enum(line[0])))

fin.close()
fout.close()


    