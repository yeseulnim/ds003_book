import sqlite3

#데이터베이스 연결
filepath = "test2.sqlite"
conn = sqlite3.connect(filepath)

#테이블 생성
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS items")
cur.execute("""CREATE TABLE items (
    item_id INTEGER PRIMARY KEY,
    name TEXT,
    price INTEGER
    )
""")
conn.commit()

#데이터 넣기
cur = conn.cursor()
cur.execute(
    "INSERT INTO items (name,price) VALUES (?,?)",
    ("Superbad 4", 22000)
)
conn.commit()

#여러 데이터 연속으로 넣기
cur = conn.cursor()
data = [("Inside Out 2", 30000), ("Furiosa", 17000), ("Dune 2", 15000)]
cur.executemany(
    "INSERT INTO items(name,price) VALUES (?,?)",
    data
)
conn.commit()

#2만원 이상 3만원 이하의 데이터 출력하기
cur = conn.cursor()
price_range = (20000, 30000)
cur.execute(
    "SELECT * FROM items WHERE price>=? and price<=?",
    price_range
)
fr_list = cur.fetchall()
for fr in fr_list:
    print(fr)