# A python program that can read two matrices of arbitrary size
# from two input disk files and multiply them if they are of
# compatible sizes. If they are of incompatible sizes,an appropriate
# error message will be printed.
# The instruction is to have two integers on the first line in each
# file which will specify the number of rows and columns in each matrix,
# and the elements in each row of the matrix will appear on a single line
# of the input file.

def lines(file):
    lines = file.readlines()
    lines = [line.rstrip() for line in list(lines)]
    return lines


def list_element(list_lines):
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

compatible_A = list(A[0])
compatible_B = list(B[0])

if compatible_A[1] == compatible_B[0]:

    list_A = list(A[1:])
    list_B = list(B[1:])

    A_one = list_element(list_A)
    B_two = list_element(list_B)

    result = [[sum(int(a) * int(b) for a, b in zip(A_row, B_col))
               for B_col in zip(*B_two)] for A_row in A_one]

    for r in result:
        print(r)

else:
    print("Error !!! , They are not compatible")
