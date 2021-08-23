# 1. practice, finding the inverse of a list

my_list = [1,2,3,4,5]
print(my_list)

#Inverse
inverse_list = []
for i in my_list:
    #print(i)
    inverse = 1/i
    inverse_list.append(inverse)
print(inverse_list)
print(sum(inverse_list))
