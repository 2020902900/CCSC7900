# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 20:22:46 2024

@author: lekhooa 2020902900
"""

def display_menu():
    print("")
    print("Please choose an arithmetic operation:")
    print("")
    print("1: Addition (+)")
    print("2: Subtraction (-)")
    print("3: Multiplication (*)")
    print("4: Normal Division (/)")
    print("5: Floor Division (//)")
    print("6: Modulus (%)")
    print("7: Exponentiation (**)")
    print("8: Squareroot (**2")

def get_operation():
    while True:
        try:
            choice = int(input("Enter the number of your choice (1-8): "))
            if choice in range(1, 9):
                return choice
            else:
                print("")
                
                print("Sorry! please select a number between 1 and 7.")
                
        except ValueError:
            
            print("Invalid input. Please enter a number.")
        
def get_numbers():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def perform_operation(choice, num1, num2):
    if choice == 1:
        return num1 + num2
    elif choice == 2:
        return num1 - num2
    elif choice == 3:
        return num1 * num2
    elif choice == 4:
        return num1 / num2
    elif choice == 5:
        return num1 // num2
    elif choice == 6:
        return num1 % num2
    elif choice == 7:
        return num1 ** num2
    elif choice == 8:
        return num1 **2
       



def is_even(number):
    return number % 2 == 0

def main():
    while True:
        display_menu()
        choice = get_operation()
        num1, num2 = get_numbers()
        result = perform_operation(choice, num1, num2)
        print("_________________________________")
        print("")
        print(f"Numbers entered: {num1} and {num2}")
        print("")
        print(f"Result of operation: {result}")
        print("")
        
        if is_even(result):
            print(f"The result {result} is even.")
        else:
            print(f"The result {result} is odd.")
        print("_________________________________")   
        again = input("Do you want to perform another operation? (yes/no): ").strip().lower()
        
        if again != 'yes':
            
            print("Thank you for using the calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
