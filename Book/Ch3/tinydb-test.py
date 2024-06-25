from tinydb import TinyDB, Query

#db연결
filepath = "test-tinydb.json"
db = TinyDB(filepath)

##기존 테이블 제거
#db.purge_table('films')

#테이블 생성/추출
table = db.table('fruits')

#테이블에 데이터 추가
table.insert({'name': 'Furiosa', 'price': 18000})
table.insert({'name': 'Inside Out 2', 'price': 33000})
table.insert({'name': 'Dune 2', 'price': 17000})

#모든 데이터 추출 및 출력
print(table.all())

#특정 데이터 추출
#Furiosa 검색
Item = Query()
res = table.search(Item.name == 'Furiosa')
print('Furiosa is ', res[0]['price'])

#가격이 20000원 이상인 항목 추출
print('2만원 이상인 항목:')
res = table.search(Item.price >= 8000)
for it in res:
    print("-", it['name'])