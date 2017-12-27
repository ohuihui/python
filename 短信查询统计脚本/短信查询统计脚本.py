import pypyodbc
SQLConnctString = r'DRIVER={SQL Server};SERVER=10.212.172.226;DATABASE=UserDataQueryProject;UID=sa;PWD=jiaohuan@288'
CommandLine = r'''SELECT Userinfo.NAME, COUNT(1) AS count
                FROM cmpp.dbo.CmSTATINFO INNER JOIN
                    Userinfo ON cmpp.dbo.CmSTATINFO.mobile = Userinfo.Num
                WHERE (cmpp.dbo.CmSTATINFO.smsport = '106585841') AND (DATEDIFF(DAY,
                    cmpp.dbo.CmSTATINFO.sendtime, GETDATE()) <= 7)
                GROUP BY Userinfo.NAME
                ORDER BY count DESC'''
sendSMSCommandPatten = r'''insert into [cmpp].[dbo].CmMETONEMTINFO (mobile,smscontent,smsport,isinqueue,userorder,sendtime,registered)
                    values ('{num}','{content}','1065858499',0,0,getdate(),1);'''
listDesNum = [13868139011]  # 放入需要发送短信的联系人
threshold = 20




def __main():
    cnxn = pypyodbc.connect(SQLConnctString, unicode_results=True)
    cur = cnxn.cursor()
    sendConfirm=False
    try:
        cur.execute(CommandLine)
        str_result = '本周短信接口用户查询次数：\r\n用户  查询次数\r\n'
        for row in cur.fetchall():
            if row[1] >= threshold:
                str_result = str_result + \
                    row[0].strip() + '  ' + str(row[1]) + '\r\n'
                sendConfirm = True

        for desNum in listDesNum:
            if sendConfirm == True:
                sendsmsCommand = sendSMSCommandPatten.format(
                    num='13868139011', content=str_result)
            else:
                sendsmsCommand = sendSMSCommandPatten.format(
                    num='13868139011', content='本周短信接口用户查询次数：\r\n本周无查询' + str(threshold) + '次及以上用户')
            cur.execute(sendsmsCommand)
            cur.commit()

    except Exception as e:
        print(e)

    finally:
        cnxn.close()


if __name__ == '__main__':
    __main()
