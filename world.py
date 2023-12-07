from agents import Car, Pedestrian, RectangleBuilding
from entities import Entity
from typing import Union
from visualizer import Visualizer

class World:
    def __init__(self, dt: float, width: float, height: float, ppm: float = 8):
        self.dynamic_agents = []
        self.static_agents = []
        self.t = 0 # simulation time
        self.dt = dt # simulation time step
        self.visualizer = Visualizer(width, height, ppm=ppm)
        
    def add(self, entity: Entity):
        if entity.movable:
            self.dynamic_agents.append(entity)
        else:
            self.static_agents.append(entity)
        
    def tick(self):
        for agent in self.dynamic_agents:
            agent.tick(self.dt)
        self.t += self.dt
    
    def render(self):
        self.visualizer.create_window(bg_color = 'gray')
        self.visualizer.update_agents(self.agents)
        
    @property
    def agents(self):
        return self.static_agents + self.dynamic_agents
        
    def collision_exists(self, agent = None):
        if agent is None:
            for i in range(len(self.dynamic_agents)):
                for j in range(i+1, len(self.dynamic_agents)):
                    if self.dynamic_agents[i].collidable and self.dynamic_agents[j].collidable:
                        if self.dynamic_agents[i].collidesWith(self.dynamic_agents[j]):
                            return True
                for j in range(len(self.static_agents)):
                    if self.dynamic_agents[i].collidable and self.static_agents[j].collidable:
                        if self.dynamic_agents[i].collidesWith(self.static_agents[j]):
                            return True
            return False
            
        if not agent.collidable: return False
        
        for i in range(len(self.agents)):
            if self.agents[i] is not agent and self.agents[i].collidable and agent.collidesWith(self.agents[i]):
                return True
        return False

    def collision_pairexists(self, agent1, agent2):
        if agent1.collidesWith(agent2):
            return True

    def collision_message(self, agent):
        message_list = []
        for i in range(len(self.agents)):
            if self.agents[i] is not agent and self.agents[i].collidable and agent.collidesWith(self.agents[i]):
                if self.agents[i].msg and self.agents[i].msg != "":
                    message_list.append(self.agents[i].msg)
                    # if "boundary" not in self.agents[i].msg:
                    #     self.agents[i].msg = ""
        return message_list

    def collision_getclass(self, agent):
        ret = []
        for i in range(len(self.agents)):
            if self.agents[i] is not agent and self.agents[i].collidable and agent.collidesWith(self.agents[i]):
                ret.append(self.agents[i].cls)
        return ret
    
    def not_collision_onclass(self, agent, cls):
        for i in range(len(self.agents)):
            if self.agents[i] is not agent and self.agents[i].collidable and agent.collidesWith(self.agents[i]):
                if cls == self.agents[i].cls:
                    return False
        return True

    
    def close(self):
        self.reset()
        self.static_agents = []
        if self.visualizer.window_created:
            self.visualizer.close()
        
    def reset(self):
        self.dynamic_agents = []
        self.t = 0