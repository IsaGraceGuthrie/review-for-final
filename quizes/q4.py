#make a new database with 3 png files and print the items in the folder and values

import dbm

db1=dbm.open("captions","c")

db1["isa"]="5.0"
db1["cadyn"]="5.2"
db1["sarah"]="5.4"

for item in db1:
    print(item,db1[item])
