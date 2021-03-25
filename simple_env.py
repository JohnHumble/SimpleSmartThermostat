# simple building energy modeling system from the sheet shared in canvas

# this should model the system found on this web-link
# http://www.sharetechnote.com/html/DE_Modeling_Example_Cooling.html

import numpy as np

class House:
    # this class would model a simple house

    def __init__(self, outside_temp=0, init_temp=30):
        # initialize rooms for the house, simple house has 3 rooms, attic, basement, main

        # TODO make this thing use normal values for a house
        self.rooms = [] # list of rooms
        self.has_therm = [] # list of bool for each room with control

        # TODO save room temperature relationships

        # initialize outside and earth temperature
        self.outside = outside_temp

    def act(self, input, dt):
        # use this to activate the heater in the main room
        for i in range(np.size(self.rooms)):
            if self.has_therm[i]:
                self.rooms[i].act(input, dt)
            else:
                self.rooms[i].update(dt)
        
        # TODO update temperatures for saved walls

    def set_out_temps(self, temps): 
        self.outside = temps
        # TODO update rooms with outside walls

class Room:
    # this class should model a single room for a building

    def __init__(self, k_vals, out_temps, initial_temp=0, heat_rate=0, cool_rate=0):
        
        # assert that k_vals is same size as out_temps
        assert(np.size(k_vals) == np.size(out_temps))

        # initialize values for room temperature
        self.temp = initial_temp
        self.heat_rate = 0
        self.cool_rate = 0

        # initialize values for border temperatures
        self.T = out_temps

        # initialize values for border inselation
        self.k = k_vals

        pass

    def act(self, input, dt):
        # this function should apply the action specified by input and give the
        # resulting output

        # input should be a 2 dimensional vector where the first entry is for
        # the heater and the second for the air conditioner.

        heat = 0
        if input[0]:
            heat += self.heat_rate
        if input[1]:
            heat -= self.cool_rate

        # the function should propagate the simulation through dt amount of
        # seconds and change the temperature values accordingly

        update(self, dt)

    def set_out_temps(self, temp):
        self.T = temp

    def update(self, dt, heat=0):
        # inputs dt: the amount of time in seconds

        # this should update the room temperature by updating the dT/dt and applying it to the room
        # dT0/dt = k1 * (T0 - T1)) + k2 * (T0 - T2) ... kn * (T0 - Tn)
        dTdt = self.get_dTdt

        # room temp should be T + (dT0/dt * dt)
        self.temp += (dTdt + heat) * dt

    def get_dTdt(self):
        # dT0/dt = k1 * (T0 - T1)) + k2 * (T0 - T2) + ... + kn * (T0 - Tn)
        return sum(np.multiply(self.k, self.temp - self.T))
