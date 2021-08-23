# A python program that calculates the decibel level
# corresponding to power levels between 1 and 20 watts in
# 0.5W steps.

import math


def frange(start, stop, step):
    x = start
    while x < stop:
        yield x
        x += step


max_power_level = 20.0
ref_power = 1
for i in frange(1.0, 2.0, 0.5):
    pass
power_levels_steps = list(frange(1.0, max_power_level, 0.5))
for i in power_levels_steps:
    decibel = 10 * math.log10(i / ref_power)
    print("Power level: ", i, " ", "Decibel level:", decibel)
