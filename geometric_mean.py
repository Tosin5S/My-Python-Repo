def accept_values():
    # global positive_inputs
    positive_values = []

    # positive_inputs
    while True:
        positive_inputs = int(input())
        if positive_inputs >= 0:
            positive_values.append(positive_inputs)
        # print(positive_values)

        elif positive_inputs < 0:
            break
        print(positive_values)
    return positive_values

    # break


def arithmetic_mean():
    print(accept_values())
    # arith_mean = sum(positive_values)


arithmetic_mean()

# mean()
