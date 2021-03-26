# simple building energy modeling system from the sheet shared in canvas

# this should model the system found on this web-link
# http://www.sharetechnote.com/html/DE_Modeling_Example_Cooling.html

import numpy as np

class House:
    # this class would model a simple house

    def __init__(self):
        # initialize rooms for the house, simple house has 3 rooms, attic, basement, main

        # TODO make this thing use normal values for a house
        self.rooms = [] # list of rooms

        # create a vector for all the temperatures
        #                 O   E   M   A   B
        self.temps = np.array([30., 20., 30., 30., 20.], dtype=np.float64)
        self.t_names = ["Outside", "ground", "main floor", "attic", "basement"]

        self.rooms.append(Room(self.temps, 2, np.array([.12,.12,.12]), np.array([0, 3, 4])))
        self.rooms.append(Room(self.temps, 3, np.array([.22,.12]), np.array([0, 2])))
        self.rooms.append(Room(self.temps, 4, np.array([.22, .12]), np.array([1, 2])))
        self.has_therm = [True, False, False]

        # initialize outside and earth temperature
        self.out_ind = 0

    def act(self, input, dt):
        # use this to activate the heater in the main room
        for i in range(np.size(self.rooms)):
            if self.has_therm[i]:
                self.rooms[i].act(input)
            else:
                self.rooms[i].set_dTdt()

        # update saved wall
        for room in self.rooms:
            room.update(dt)

        # TODO update temperatures for saved walls

    def set_outside_temp(self, temp):
        self.temps[self.out_ind] = temp

    def get_temps(self):
        return self.temps, self.t_names

class Room:
    # this class should model a single room for a building

    def __init__(self, temps, temp_ind, k_vals, out_temp_inds, heat_rate=0, cool_rate=0):
        
        # assert that k_vals is same size as out_temps
        assert(np.size(k_vals) == np.size(out_temp_inds))

        # initialize values for room temperature
        self.temp_ind = temp_ind
        self.heat_rate = 0
        self.cool_rate = 0

        # initialize values for border temperatures
        self.out_ind = out_temp_inds
        self.temp_vec = temps

        # initialize values for border inselation
        self.k = k_vals

        self.dTdt = 0

        pass

    def act(self, input):
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
        self.set_dTdt(heat=heat)

        pass

    def set_dTdt(self, heat=0):
        self.dTdt = self.get_dTdt() + heat

    def update(self, dt):
        # inputs dt: the amount of time in seconds

        # this should update the room temperature by updating the dT/dt and applying it to the room
        # dT0/dt = k1 * (T0 - T1)) + k2 * (T0 - T2) ... kn * (T0 - Tn)
        #dTdt = self.get_dTdt

        # room temp should be T + (dT0/dt * dt)
        self.temp_vec[self.temp_ind] += self.dTdt * dt

    def get_dTdt(self):
        T = self.temp_vec[self.out_ind]
        temp = self.temp_vec[self.temp_ind]

        # dT0/dt = k1 * (T0 - T1)) + k2 * (T0 - T2) + ... + kn * (T0 - Tn)
        return sum(np.multiply(self.k, T - temp))
