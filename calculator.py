# calculator.py
import numpy as np
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y
#def  gcd(x,y):
    #while b:
        #a,b =b.a%b
    #return a

def matrix_subtraction(A, B):
    return np.subtract(A, B)

def main():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Matrix Subtraction")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice in ['1', '2', '3', '4' , '5']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")

        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")

        elif choice == '4':
            try:
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            except ValueError as e:
                print(e)

        elif choice =='5':
            print(f'matrix subtraction of {num1} and {num2} is{matrix_subtraction(num1, num2)}')
    else:
        print("Please enter a valid input")

if __name__ == "__main__":
    main()
