from numpy import random

randomNum = random.randint(1,50)

print('Guess number between 1 and 50')

for i in range(1,7):
    if i < 7:
        guess = int(input("Guess the number: "))
        if guess == randomNum:
            print("Correct!")
            exit()
        elif guess < randomNum:
            print("Too low")
        else:
            print("Too high")
print('Unlucky, number was ' + str(randomNum))
