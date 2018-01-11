SELECT  cmpp.dbo.CmSTATINFO.sendtime,cmpp.dbo.CmSTATINFO.smscontent,Userinfo.NAME
FROM cmpp.dbo.CmSTATINFO INNER JOIN
      Userinfo ON cmpp.dbo.CmSTATINFO.mobile = Userinfo.Num
WHERE (cmpp.dbo.CmSTATINFO.smsport = '106585841') AND (DATEDIFF(DAY,
      cmpp.dbo.CmSTATINFO.sendtime,  '2018/01/08 00:00' ) <= 7)
order by Name