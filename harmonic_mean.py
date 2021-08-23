# A python program for calculating the harmonic mean for a set of numbers.

positive_values = []
print("I want to calculate the harmonic mean of a set of numbers")
decision = input("Enter 'y' for yes or 'n' for no: ")
while decision == "y":
    positive_input = int(input("Enter a positive value or quit with a negative value: "))

    if positive_input >= 0:
        positive_values.append(positive_input)
        print(positive_values)
        inverse_list = []
        for i in positive_values:
            inverse = 1 / i
            inverse_list.append(inverse)

    else:
        # print("Bye Sir")
        break

    print(positive_values)
    sum_of_inverse = sum(inverse_list)
    # print(sum_of_inverse)
    length = len(positive_values)
    harmonic_mean = length / sum_of_inverse

else:
    if decision == "n":
        print("Thanks, Have a nice day Sir.")
    else:
        print("You pressed another thing apart from 'n' ")

print("Your harmonic mean is : ", harmonic_mean)
