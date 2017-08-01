#Write a Python function to find the Max of three numbers.


print ('*' * 40)
print ("FIND THE MAX NUMBER OUT OF 3 NUMBERS")
print ('*' * 40)

x = int(input("please enter 1st number: "))
y = int(input("please enter 2nd number: "))
z = int(input("please enter 3rd number: "))
def max_of_two(x, y):
    if x > y:
        return x
    else:
        return y
def max_of_three(x, y, z):
    return max_of_two(z, max_of_two(x, y))

print ("Max number is:", max_of_three(x,y,z))