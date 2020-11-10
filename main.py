import matplotlib.pyplot as plt
import numpy as np
import math
import os
import time

class Aircraft(object):

    def __init__(self, name, alt, speed, pos):
        self.name = str(name)
        self.alt = int(alt)
        self.speed = int(speed)
        self.pos = tuple(pos)
    
    def get_name(self):

        return self.name
    
    def get_alt(self):

        return self.alt
    
    def get_speed(self):

        return self.speed
    
    def get_pos(self):

        return self.pos

if __name__ == "__main__":

    a1 = Aircraft("Qantas", 2000, 10, (10,5))

    print(a1.name)
    print(a1.alt)
    print(a1.speed)
    print(a1.pos)


