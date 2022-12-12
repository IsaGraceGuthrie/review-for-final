import dbm

db1=dbm.open("caption","c")

db1["mouse.png"]="cheese"
db1["house.png"]="with a red door"
db1["dance.png"]="with cadyn"

for item in db1:
    print(item,db1[item])
