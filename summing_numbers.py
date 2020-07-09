# Defining my_sum function:


def my_sum(*numbers):
    output = 0
    for each_number in numbers:
        output += each_number
    return output


print(my_sum(1, 2, 3, 4))