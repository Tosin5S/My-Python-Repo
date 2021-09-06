def lines(file):
    lines = file.readlines()
    lines = [line.rstrip() for line in list(lines)]

    list_lines = list(lines[1:])
    x = []
    for i in list_lines:
        elements = list(i)
        x.append(elements)
    return x


first_matrix = input("Enter your first txt filename: ")
second_matrix = input("Enter your second txt filename: ")

f_first = open(first_matrix, "r")
f_second = open(second_matrix, "r")
A = lines(f_first)
B = lines(f_second)

result = [[sum(int(a) * int(b) for a, b in zip(A_row, B_col))
           for B_col in zip(*B)] for A_row in A]

for r in result:
    print(r)
