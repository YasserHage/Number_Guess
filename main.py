import numpy as num
play = True
while play == True:
    hiddenNumber = num.random.randint(0,10)
    print("\ntry to guess the hidden number")
    for turn in range(5):
        print("Turn " + str(turn + 1) + ":\n")
        number = input()
        if str(number) == str(hiddenNumber):
            print("Congratulations! You won\n")
            break
        elif str(number) < str(hiddenNumber):
            print("The number were too low, try a greeter one!\n")
        else:
            print("The number were too high, try a lesser one!\n")
        if turn == 4:
            print("Too bad you've lost!")
    print("Do you want to play again? (y/n)\n")
    playAgain = input()
    if playAgain == "y":
        play = True
    else:
        print("Bye then!")
        play = False