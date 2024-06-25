#3장 '데이터 소스의 서식과 가공' 실습
import sqlite3

#sqlite db 연결
dbpath = "test.sqlite"
conn = sqlite3.connect(dbpath)

#table 생성 및 데이터 입력
cur = conn.cursor()
cur.executescript("""
/*테이블이 이미 있을 경우 제거 */
DROP TABLE IF EXISTS items;

/*테이블 생성*/
CREATE TABLE items(
    item_id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    price INTEGER
);

/*데이터 삽입*/
INSERT INTO items(name,price) VALUES ('DUNE 2', 15000);
INSERT INTO items(name,price) VALUES ('Furiosa', 18000);
INSERT INTO items(name,price) VALUES ('Inside Out 2', 16000);
""")

#위 조작을 데이터베이스에 반영
conn.commit()

#데이터 추출
cur = conn.cursor()
cur.execute("SELECT item_id, name, price FROM items")
item_list = cur.fetchall()

#출력
for it in item_list:
    print(it)