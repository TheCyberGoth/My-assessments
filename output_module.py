def display_output(summ, diff, prod, quot, num1, num2):
    print(f"The sum of {num1} and {num2} is {summ}")
    print(f"The difference between {num1} and {num2} is {diff}")
    print(f"The product of {num1} and {num2} is {prod}")
    print(f"The quotient of {num1} and {num2} is {quot}")
    with open('calculations.txt', 'a') as file:
        file.write(f"The sum of {num1} and {num2} is {summ}\n")
        file.write(f"The difference between {num1} and {num2} is {diff}\n")
        file.write(f"The product of {num1} and {num2} is {prod}\n")
        file.write(f"The quotient of {num1} and {num2} is {quot}\n")