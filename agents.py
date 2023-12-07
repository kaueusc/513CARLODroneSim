from entities import RectangleEntity, CircleEntity, RingEntity
from geometry import Point

# For colors, we use tkinter colors. See http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter

class Car(RectangleEntity):
    def __init__(self, center: Point, heading: float, color: str = 'red'):
        size = Point(4., 2.)
        movable = True
        friction = 0.06
        super(Car, self).__init__(center, heading, size, movable, friction)
        self.color = color
        self.collidable = True

        self.state = "start"

    def print_wstep(self, message, timestep, addCoord=False):
        coordString = ""
        if addCoord:
            coordString = f"\tDrone Coord:{round(self.center.x,2)},{round(self.center.y,2)}"
        print(f"{timestep}: {message} {coordString}")
    
    def auto_step(self, w, timestep):
        #print(self.heading)

        if "topbound" in w.collision_getclass(self) and (self.state == "straightup" or self.state == "start"):
            #self.state = "ontopbound"
            self.state = "turnright"
        
        # elif self.state =="ontopbound" and w.not_collision_onclass(self, "topbound"):
        #     self.state = "turnright"

        elif self.state == "turnright":
            self.set_control(-0.3,0)
            if self.heading > 3.14 and self.heading < 4.71238898038 + 0.1:
                self.heading = 4.71238898038
                self.set_control(0,0)
                self.print_wstep("stop turning right",timestep)
                self.state = "straightdown"

        # elif self.state == "straightdown":
        #     self.heading = 4.71238898038
        #     self.set_control(0,0)

        elif "botbound" in w.collision_getclass(self) and self.state == "straightdown":
            #self.state = "onbotbound"
            self.state = "turnleft"

        # elif self.state =="onbotbound" and w.not_collision_onclass(self, "botbound"):
        #     self.state = "turnleft"

        elif self.state == "turnleft":
            self.set_control(0.3,0)
            if self.heading < 3.14 and self.heading > 1.57079632679 - 0.1:
                self.heading = 1.57079632679
                self.set_control(0,0)
                self.print_wstep("stop turning left",timestep)
                self.state = "straightup"

        # elif self.state == "straightup":
        #     self.heading = 1.57079632679
        #     self.set_control(0,0)

        #print(self.center)
        message_list = w.collision_message(self)
        for message in message_list:
            self.print_wstep(message,timestep,addCoord=True)

class Pedestrian(CircleEntity):
    def __init__(self, center: Point, heading: float, color: str = 'LightSalmon3'): # after careful consideration, I decided my color is the same as a salmon, so here we go.
        radius = 0.5
        movable = True
        friction = 0.2
        super(Pedestrian, self).__init__(center, heading, radius, movable, friction)
        self.color = color
        self.collidable = True
        
class RectangleBuilding(RectangleEntity):
    def __init__(self, center: Point, size: Point, color: str = 'gray26', cls = None, msg = None):
        heading = 0.
        movable = False
        friction = 0.
        super(RectangleBuilding, self).__init__(center, heading, size, movable, friction)
        self.color = color
        self.collidable = True
        self.cls = cls
        self.msg = msg
        
class CircleBuilding(CircleEntity):
    def __init__(self, center: Point, radius: float, color: str = 'gray26', cls = None, msg = None):
        heading = 0.
        movable = False
        friction = 0.
        super(CircleBuilding, self).__init__(center, heading, radius, movable, friction)
        self.color = color
        self.collidable = True
        self.cls = cls
        self.msg = msg

class RingBuilding(RingEntity):
    def __init__(self, center: Point, inner_radius: float, outer_radius: float, color: str = 'gray26', cls = None, msg = None):
        heading = 0.
        movable = False
        friction = 0.
        super(RingBuilding, self).__init__(center, heading, inner_radius, outer_radius, movable, friction)
        self.color = color
        self.collidable = True
        self.cls = cls
        self.msg = msg

class Painting(RectangleEntity):
    def __init__(self, center: Point, size: Point, color: str = 'gray26', heading: float = 0.):
        movable = False
        friction = 0.
        super(Painting, self).__init__(center, heading, size, movable, friction)
        self.color = color
        self.collidable = False

class CirclePainting(CircleEntity):
    def __init__(self, center: Point, radius: float, color: str = 'gray26'):
        heading = 0.
        movable = False
        friction = 0.
        super(CirclePainting, self).__init__(center, heading, radius, movable, friction)
        self.color = color
        self.collidable = False
