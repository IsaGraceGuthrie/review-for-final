class Point:
    "a point in 3-d space"

p=Point()

p.x=3.0
p.y=2.0
p.z=7.0

def where_at(space):
    a=space.x**3
    b=space.y+9
    c=space.z-33
    total=a+b+c
    print(total)
where_at(p)
