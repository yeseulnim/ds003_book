import MySQLdb

#mysql 연결
conn = MySQLdb.connect(
    user = "root",
    password = "test-password",
    host = "localhost",
    db = "test"
)

#커서 추출
cur = conn.cursor()

#테이블 생성
cur.execute('DROP TABLE items')
cur.execute('''
    CREATE TABLE items(
        item_id INTEGER PRIMARY KEY AUTO_INCREMENT,
        name TEXT,
        price INTEGER
    )
''')

#데이터 추가하기
data = [("Inside Out 2", 30000), ("Furiosa", 17000), ("Dune 2", 15000)]
for i in data:
    cur.execute("INSERT INTO items(name,price) VALUES (%s,%s)", i)

#데이터 추출하기
cur.execute("SELECT * FROM items")
for row in cur.fetchall():
    print(row)