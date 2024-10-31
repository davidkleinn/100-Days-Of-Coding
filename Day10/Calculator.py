from calculatorAscii import calcLogo
import os


def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2


opDic = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
    }

def calculator():
    
    print(calcLogo)
    n1 = float(input("Type your number:\n"))

    while True:

        print("")

        op = input("Choose the operation you want to do.\nType '+', '-', '*' or '/':\n")

        n2 = float(input("Type other number:\n"))

        ans = opDic[op](n1, n2)

        print(f"{n1} {op} {n2} = {ans}")

        choice = input(f"Type 'y' to continue calculating with {ans}, or type 'n' to do a new calculation:\n")

        if choice == "y":
            n1 = ans
        else:
            os.system('cls')
            calculator()
            break

calculator()
            
            
