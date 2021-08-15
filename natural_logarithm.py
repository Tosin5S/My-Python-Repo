import math


def accept_values():
    while True:
        legal_input = int(input("Please enter a legal value: "))
        if legal_input <= 0:
            y = math.log(1 / (1 - legal_input))
            print("The result is: ", y)

        elif legal_input > 0:
            break


accept_values()
