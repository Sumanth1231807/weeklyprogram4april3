import cmath
import math

def square_root(x):
    s=math.sqrt(x)
    return s

def quadratic_equation(a,b,c):
    d = (b ** 2) - (4 * a * c)
    sol1 = (-b - cmath.sqrt(d)) / (2 * a)
    sol2 = (-b + cmath.sqrt(d)) / (2 * a)
    return sol1,sol2

def cels_to_farh(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

def pos_neg_zero(x):
    if x > 0:
        return "positive"
    elif x == 0:
        return "zero"
    else:
        return "negative"


def natural_num(num):
    def recur_sum(n):
        if n <= 1:
            return n
        else:
            return n + recur_sum(n - 1)
    if num < 0:
        return "Invalid"
    else:
        return recur_sum(num)

if __name__=="__main__":
    print("Finding Square Root")
    x=int(input("Enter the Number :"))
    sqrt=square_root(x)
    print(sqrt)

    print("Finding Quadratic Equation")
    a=int(input("Enter num 1 :"))
    b=int(input("Enter num 2 :"))
    c=int(input("Enter num 3 :"))
    quateq=quadratic_equation(a,b,c)
    print(quateq)

    print("Converting Celsies to Fahrenheit")
    celsius=float(input("Enter the Celsius :"))
    cel=cels_to_farh(celsius)
    print(cel)

    print("Finding given number is Positive, Negative or Zero")
    x = int(input("Enter the Number :"))
    posneg=pos_neg_zero(x)
    print(posneg)

    print("Find Sum of Natural Numbers Using Recursion")
    num=int(input("Enter the Number :"))
    natnum=natural_num(num)
    print(natnum)


