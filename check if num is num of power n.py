from math import floor, log

def is_power_of_n(num, power):
    if num <= 0:
        return 0
    else:
        p = int(floor(log(num) / log(power)))
        power_floor = pow(power, p)
        power_ceil = power_floor * power
        if power_floor == num or power_ceil == num:
            return True
        return False

is_power_of_n(27, 3)