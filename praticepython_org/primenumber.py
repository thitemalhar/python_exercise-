print ('*' * 40)
print ("CHECK PRIME NUMBER")
print ('*' * 40)
num = int(input("Please enter number to check if it\'s prime number: "))

z = [x for x in range(2, num) if (num % x) == 0]

def is_prime(num):
    if num > 1:
        if len(z) == 0:
            print ("PRIME number")
        elif len(z) != 0:
            print ("NOT PRIME number")
    else:
        print ("NOT prime number")

is_prime(num)