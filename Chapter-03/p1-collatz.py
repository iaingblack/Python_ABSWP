def collatz(number):
    iterations = 0
    while number != 1:
        iterations += 1
        if number % 2 == 0:
            number = number // 2
            print(str(number))
        else:
            number = (number * 3 + 1)
            print(str(3 * number + 1))

    print("Iterations was " + str(iterations))

userNum = int(input("Enter a number: "))
collatz(userNum)


