import MySQLdb

con = MySQLdb.connect(
    host='119.23.13.34',
    user='news',
    passwd='meiyoumima',
    port=3306,
    db='newsdb',
    charset='utf8'
    )
#执行查询前， 需要先获取cursor
cursor = con.cursor()
cursor.execute('SELECT * FROM `news`')
rest = cursor.fetchone()
print(rest)
