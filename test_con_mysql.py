import MySQLdb

con = MySQLdb.connect(
    host='119.23.13.34',
    user='news',
    passwd='lovedbp4',
    port=3306,
    db='newsdb',
    charset='utf8'
    )

cursor = con.cursor()
cursor.execute('SELECT * FROM `news`')
rest = cursor.fetchone()
print(rest)
