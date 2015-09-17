"""Fibonacci Sequence Calculator- accepts a number and displays it's fibonacci sequence
   By Dakota Mitchem"""


def user_input():
    # Collects input from the user
    in_number = input("How many digits of the Fibonacci Sequence would you like calculated?")
    # Starts the logic module with the dependent variable
    logic(in_number)


    # Defines the logic module and dependent variable
def logic(in_number):
    # Creates the sequence list
    sequence = [0]
    # Prints sequence if user_input = 0
    if in_number == 0:
        print sequence
    # Adds 1 to the sequence list if user_input = 1 and prints it
    elif in_number == 1:
        sequence.append(1)
        print sequence
    # Adds 1 to the sequence list if user input is greater than 1
    elif in_number > 1:
        sequence.append(1)
        num1 = 1
        num2 = 0
        num3 = num1 + num2
    # Calculates fibonacci numbers up to inputted variable and adds them to the sequence list
        for x in range(1, int(in_number)):
            num1 = int(num2)
            num2 = int(num3)
            num3 = num1 + num2
            sequence.append(int(num3))
    # Prints the list sequence
        print sequence

    # Launches th user_input module
user_input()
