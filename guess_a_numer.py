import random

guess = 0
count = 0

a = random.randint(1 ,10)

while guess != a and guess != "exit":
    guess = input("Enter a number: ")

    if guess == 'exit':
        break

    guess = int(guess)
    count += 1

    if guess < a:
        print ("You guessed it low")
    elif guess > a:
        print ("You guessed it high")
    elif guess == a:
        print("you guessed it right")
        print ("It took you", count, 'retries')