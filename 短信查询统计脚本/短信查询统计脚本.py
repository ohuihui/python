import pypyodbc
SQLConnctString = r'DRIVER={SQL Server};SERVER=10.212.172.226;DATABASE=UserDataQueryProject;UID=sa;PWD=jiaohuan@288'
CommandLine = r'''SELECT Userinfo.NAME, COUNT(1) AS count
                FROM cmpp.dbo.CmSTATINFO INNER JOIN
                    Userinfo ON cmpp.dbo.CmSTATINFO.mobile = Userinfo.Num
                WHERE (cmpp.dbo.CmSTATINFO.smsport = '106585841') AND (DATEDIFF(DAY,
                    cmpp.dbo.CmSTATINFO.sendtime, GETDATE()) <= 7)
                GROUP BY Userinfo.NAME
                ORDER BY count DESC'''


def __main():
    cnxn = pypyodbc.connect(SQLConnctString, unicode_results=True)
    cur = cnxn.cursor()
    try:
        cur.execute(CommandLine)
        for row in cur.fetchall():
            print(row)

    except Exception as e:
        print(e)

    finally:
        cnxn.close()



if __name__ == '__main__':
    __main()
