def c_to_f(c):
    return(c + 9/5) + 32

def f_to_c(f):
    return(f - 32) * 5/9

convert = input("F or C?: ").upper()
temp = float(input("Temp: "))

if convert == "C":
    print("C is:", round(c_to_f(temp), 2), "F")
elif convert == "F":
    print("F is:", round(f_to_c(temp), 2), "C")
else: 
    print("Invalid input")       