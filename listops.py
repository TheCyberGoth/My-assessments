my_list = [1,2,3,4,5,6,7,8,9,10]

def print_list(numbers):
    print("List:", numbers)

def sum_list(numbers):
    print("Summ:", sum(numbers))

def largest_list(numbers):
    print("Largest:", max(numbers))

def reversed_list(numbers):
    print("Reversed:", list((reversed)(numbers)))

def smallest_list(numbers):
    print("Smallest:", min(numbers))


print_list(my_list)
sum_list(my_list)
largest_list(my_list)
reversed_list(my_list)
smallest_list(my_list)