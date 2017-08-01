#Write a Python function to sum all the numbers in a list

numbers = [int(x) for x in input("please enter number to get the sum of numbers: ").split()]

def sum(numbers):
    total = 0
    for a in numbers:
        total = total + a
    return total

print ("Total is: ", sum(numbers))