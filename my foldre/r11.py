import dbm

db1=dbm.open("captions","c")

db1["cheese.png"]="a mouse"
db1["bread.png"]="a gluten free bread"
db1["fruit.png"]="strawberries"

for item in db1:
    print(item,db1[item])
