
class Ambulance:
    """An Ambulance to the hosptial"""

myAmbulance=Ambulance()

myAmbulance.priority =0
myAmbulance.speed = 160
myAmbulance.capacity =1

def velocity(car):
    x=-10*(1-car.priority)
    y=2.37*(car.speed/10)**3.98
    z=30*(car.capacity+1.2)
    controlled_velocity= x + y + z
    print(controlled_velocity)



velocity(myAmbulance)
