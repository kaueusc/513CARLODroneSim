import numpy as np
from world import World
from agents import Car, RectangleBuilding, Pedestrian, Painting, CircleBuilding, CirclePainting, RingBuilding
from geometry import Point
import time

human_controller = False

dt = 0.1 # time steps in terms of seconds. In other words, 1/dt is the FPS.
w = World(dt, width = 120, height = 120, ppm = 6) # The world is 120 meters by 120 meters. ppm is the pixels per meter.

# Let's add some sidewalks and RectangleBuildings.
# A Painting object is a rectangle that the vehicles cannot collide with. So we use them for the sidewalks.
# A RectangleBuilding object is also static -- it does not move. But as opposed to Painting, it can be collided with.
# For both of these objects, we give the center point and the size.

#background pasture/landscape
w.add(Painting(Point(60,60), Point(120, 120), color='tan')) 

#Tree boundaries as paintings
# w.add(Painting(Point(10, 10), Point(30, 30), 'tan'))
# w.add(Painting(Point(10, 30), Point(30, 30), 'tan'))

# #Trees as paintings
# w.add(Painting(Point(10, 10), Point(10, 10), 'green'))
# w.add(Painting(Point(10, 30), Point(10, 10), 'yellow'))

def createTreeSens(x,y,treesize, sensradius, treecolor, number):
    basemsg = "detecting tree"
    if treecolor == 'yellow':
        basemsg = "detecting infected tree"
    sens = RingBuilding(Point(x,y), treesize, sensradius, color='tan', msg=basemsg+str(number))
    w.add(sens)
    tree = CircleBuilding(Point(x,y), 5, color=treecolor, msg="collided with tree"+str(number))
    w.add(tree)

createTreeSens(23,30,5,15,'green',1)
createTreeSens(23,50,5,15,'green',2)
createTreeSens(23,70,5,15,'yellow',3)
createTreeSens(23,90,5,15,'green',4)

createTreeSens(49,30,5,15,'yellow',5)
createTreeSens(49,50,5,15,'green',6)
createTreeSens(49,70,5,15,'green',7)
createTreeSens(49,90,5,15,'green',8)


createTreeSens(75,30,5,15,'green',9)
createTreeSens(75,50,5,15,'yellow',10)
createTreeSens(75,70,5,15,'yellow',11)
createTreeSens(75,90,5,15,'green',12)


createTreeSens(101,30,5,15,'green',13)
createTreeSens(101,50,5,15,'green',14)
createTreeSens(101,70,5,15,'green',15)
createTreeSens(101,90,5,15,'yellow',16)

#Trees and sensing boundary
# sens1 = RingBuilding(Point(25,30), 5, 15, color='tan', msg="detecting tree1")
# w.add(sens1)
# tree1 = CircleBuilding(Point(25,30), 5, color='green', msg="collided with tree1")
# w.add(tree1)

topboundary = RectangleBuilding(Point(60,100), Point(120, 1), color='blue', cls = "topbound", msg="top boundary")
w.add(topboundary)

botboundary = RectangleBuilding(Point(60,20), Point(120, 1), color='blue', cls = "botbound", msg="bot boundary")
w.add(botboundary)


# w.add(Painting(Point(71.5, 106.5), Point(97, 27), 'green')) # We build a sidewalk.
#w.add(RectangleBuilding(Point(10,10), Point(10, 10), color='green')) # The RectangleBuilding is then on top of the sidewalk, with some margin.

# # Let's repeat this for 4 different RectangleBuildings.
# w.add(Painting(Point(8.5, 106.5), Point(17, 27), 'green'))
# w.add(RectangleBuilding(Point(7.5, 107.5), Point(15, 25), color='green'))

# w.add(Painting(Point(8.5, 41), Point(17, 82), 'gray80'))
# w.add(RectangleBuilding(Point(7.5, 40), Point(15, 80), color='green'))

# w.add(Painting(Point(71.5, 41), Point(97, 82), 'gray80'))
# w.add(RectangleBuilding(Point(72.5, 40), Point(95, 80), color='green'))

# Let's also add some zebra crossings, because why not.
# w.add(Painting(Point(18, 81), Point(0.5, 2), 'white'))
# w.add(Painting(Point(19, 81), Point(0.5, 2), 'white'))
# w.add(Painting(Point(20, 81), Point(0.5, 2), 'white'))
# w.add(Painting(Point(21, 81), Point(0.5, 2), 'white'))
# w.add(Painting(Point(22, 81), Point(0.5, 2), 'white'))

# A Car object is a dynamic object -- it can move. We construct it using its center location and heading angle.
c1 = Car(Point(10,20), np.pi/2)
w.add(c1)

# c2 = Car(Point(118,90), np.pi, 'blue')
# c2.velocity = Point(3.0,0) # We can also specify an initial velocity just like this.
# w.add(c2)

# c3 = Car(Point(50,90), np.pi, 'black')
# w.add(c3)

# c4 = Car(Point(120,80), np.pi, 'green')
# w.add(c4)

# Pedestrian is almost the same as Car. It is a "circle" object rather than a rectangle.
# p1 = Pedestrian(Point(28,81), np.pi)
# p1.max_speed = 10.0 # We can specify min_speed and max_speed of a Pedestrian (and of a Car). This is 10 m/s, almost Usain Bolt.
# w.add(p1)

w.render() # This visualizes the world we just constructed.


if not human_controller:
    # Let's implement some simple scenario with all agents
    #p1.set_control(0, 0.22) # The pedestrian will have 0 steering and 0.22 throttle. So it will not change its direction.
    c1.set_control(0, 2)
    #c2.set_control(0, 0.05)
    for k in range(800):
        c1.auto_step(w,k)

        # All movable objects will keep their control the same as long as we don't change it.
        # if k == 100: # Let's say the first Car will release throttle (and start slowing down due to friction)
        #     c1.set_control(0, 0)
        # elif k == 200: # The first Car starts pushing the brake a little bit. The second Car starts turning right with some throttle.
        #     c1.set_control(0, -0.02)
        # elif k == 325:
        #     c1.set_control(0, 0.8)
        #     #c2.set_control(-0.45, 0.3)
        # elif k == 367: # The second Car stops turning.
        #     #c2.set_control(0, 0.1)
        #     pass
        w.tick() # This ticks the world for one time step (dt second)
        w.render()
        time.sleep(dt/4) # Let's watch it 4x

        # if w.collision_exists(p1): # We can check if the Pedestrian is currently involved in a collision. We could also check c1 or c2.
        #     print('Pedestrian has died!')
        # elif w.collision_exists(): # Or we can check if there is any collision at all.
        #     print('Collision exists somewhere...')
        # if w.collision_exists():
        #     print('Collision exists somewhere...')
        # else:
        #     print('no collision')
    w.close()

else: # Let's use the steering wheel (Logitech G29) for the human control of car c1
    #p1.set_control(0, 0.22) # The pedestrian will have 0 steering and 0.22 throttle. So it will not change its direction.
    #c2.set_control(0, 0.35)
    
    from interactive_controllers import KeyboardController
    controller = KeyboardController(w)
    for k in range(1000):
        c1.set_control(controller.steering, controller.throttle)
        c1.auto_step(w,k)
        w.tick() # This ticks the world for one time step (dt second)
        w.render()
        time.sleep(dt/4) # Let's watch it 4x
        
        # if w.collision_exists():
        #     if w.collision_pairexists(c1,tree1):
        #         print('Collided with tree!')
        #     elif w.collision_pairexists(c1, sens1):
        #         print('Within detection radius of tree 1')
        #     else:
        #         print('Collision exists somewhere...')
        # else:
        #     print('no collision')
        # if w.collision_exists():
        #     # import sys
        #     # sys.exit(0)
        #     print('Collision exists somewhere...')