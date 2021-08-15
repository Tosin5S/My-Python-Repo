def accept_values():
    positive_values = []

    while True:
        positive_inputs = int(input("Please enter a value or terminate with a negative value: "))
        if positive_inputs >= 0:
            positive_values.append(positive_inputs)

        elif positive_inputs < 0:
            break
        print(positive_values)
    summation = sum(positive_values)
    length = len(positive_values)
    arithmetic_mean = summation / length
    print("Your arithmetic mean is: ", arithmetic_mean)

    product = 1
    for x in positive_values:
        product *= x
    # print(product)
    geometric_mean = product ** (1 / length)
    print("Your geometric mean is: ", geometric_mean)


accept_values()
