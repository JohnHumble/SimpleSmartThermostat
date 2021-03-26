import numpy as np

from house import House

def simulate(low=20.0, high=30.0):
    house = House()
    
    minutes_in_day = 1440
    step = (high - low) / minutes_in_day * 2
    morning = np.arange(low,high, step)
    afternoon = np.arange(high, low, -step)
    o_temps = np.concatenate((morning, afternoon))

    # TODO get some real wold temperature data

    for i in range(minutes_in_day):
        house.set_outside_temp(o_temps[i])

        for j in range(60):
            house.act(np.array([0,0]), 1)

        temps, names = house.get_temps()

        if i % 100 == 0:
            for i in range(len(names)):
                print(f"{names[i]} : {temps[i]}")
            print()

if __name__ == "__main__":
    simulate()
