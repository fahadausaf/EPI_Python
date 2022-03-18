# Compute x^y

def compute_power(x, y):
    result = 1.0
    power = y
    if y < 0:
        power = -power
        x = 1.0 / x
    while power:
        print(power)
        print(x)
        print(result)
        if power & 1:
            print("yes")
            result *= x
        x = x * x
        power = power >> 1
        print()
    return result

print(compute_power(2,3))