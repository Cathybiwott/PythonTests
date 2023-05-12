# Write a function that takes an unknown number of arguments and returns their sum.
def sum_args(*args):
    return sum(args)

print(sum_args(11, 20, 3)) 
print(sum_args(10, 50, 30, 60))

# Write a function that takes two arguments, the first being a string and the second 
# being an unknown number of integers. The function should return a new string 
# where the integers have been added to the original string.
def add_numbers_to_string(string, *args):
    return string + "".join(str(i) for i in args)

print(add_numbers_to_string("My lucky number is ", 6)) 
print(add_numbers_to_string("The numbers are: ", 6,1,2))




# Write a function that takes an unknown number of keyword arguments and returns a dictionary 
# where the keys are the argument names and the values are the argument values.
def kwargs_to_dict(**kwargs):
    return kwargs

print(kwargs_to_dict(g=10, k=12, y=6)) 
print(kwargs_to_dict(fruit="Kiwi", amount=25)) 




# Write a function that takes a function and an unknown number of arguments, and returns 
# the result of calling the function with the arguments.
def call_function_with_args(func, *args):
    return func(*args)

def subtraction(a, b, c):
    return a - b - c

print(call_function_with_args(subtraction, 9, 3, 1)) 



# Write a function that takes a list of integers and an unknown number of keyword arguments. 
# The function should return a new list where each integer in the original list has been 
# multiplied by the value of the corresponding keyword argument.
def multiply_list_by_keyword_args(int_list, **kwargs):
    new_list = []
    for num in int_list:
        product = num
        for key, value in kwargs.items():
            product *= value
        new_list.append(product)
    return new_list

result_list = multiply_list_by_keyword_args([2, 4, 7], x=2, y=3, z=4)
print(result_list)




# Write a function that takes a list of integers and an unknown number of additional integers as arguments. 
# The function should return the index of the first occurrence of the sum of the list and the additional integers
def sum_index(lst, *args):
    total = sum(lst) + sum(args)
    try:
        index = lst.index(total)
        return index
    except ValueError:
        return -1

list = [1, 2, 3, 4, 5]
result = sum_index(list, 5, 4, 3)
print(result) 






# Write a function that takes an unknown number of keyword arguments, each with a string value. The function should concatenate all the strings and return the resulting string.
def concatenate_strings(**kwargs):
    return "".join(kwargs.values())

print(concatenate_strings(n="Come ", k="here ", t="Cathy"))
