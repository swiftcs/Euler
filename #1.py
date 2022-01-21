import random


def challenge1():
    x = 0
    for i in range(1, 1001):
        if i % 3 == 0 or i % 5 == 0:
            if i < 1000:
                x = x + i
                print(x)
    print(x)

