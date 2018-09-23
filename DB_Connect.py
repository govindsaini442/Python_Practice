import cx_Oracle
host="localhost"
port = 1521
SID = "orcl"
user="system"
passwd="redhat"
dsn_tns = cx_Oracle.makedsn(host, port, SID)
print(dsn_tns)

con = cx_Oracle.connect(user, passwd, dsn_tns)
print(con.version)
cur = con.cursor()
'''cur.execute("select * from TAB")
print(con.version)
for result in cur:
    print(result)'''
con.close()