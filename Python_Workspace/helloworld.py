import time

#initialization
goal = 12
guess = 0

while True:
    guess = int(input("Enter your guess: "))
    if guess == goal:
        print("You're right!")
        break
    if guess < goal:
        print("Too low!")
    elif guess > goal: 
        print("Too high!")
    time.sleep(1)
    print("Try again!")
 
