class Point:
    """Represents a point in a 2-D space"""
print(type(Point))
#<class 'type'>

mypoint=Point()
print(type(mypoint))
#<class '__main__.Point'>

mypoint.x= 0
mypoint.y= 2

print(mypoint.x)
print(mypoint.y)
# 0
# 2

print("(%d,%d)"%(mypoint.x,mypoint.y))
#(0,2)

mypoint.x= 3
mypoint.y= 4
import math

def distance_from_origin(p):
    distance=math.sqrt(p.x**2+p.y**2)
    print(distance)

distance_from_origin(mypoint)
#5.0
