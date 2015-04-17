__author__ = 'ZheWu'
name = input("Hello, what is your name?")
print("Hello, " + name + "! Let's play a game!")
print("Think of random number form 1 to 100, and I will try to guess it!")
play = True
small = 1                   #set up the range of the numbers
big = 100
n = 1
while ( play ):             # To check the user want to play again or not.
    middle = int(( small + big) / 2 )
    print("Is it :", middle, "?(yes or no)")
    answer = input()
    if answer == "yes":     #get the right number
        print("yeah! I got it in ", n, "times")
        playAgain = input("Do you want to play again (Yes or no)")
        if playAgain == "no":
            play = False
            print("Thanks for playing, Bye-bye")
        else:               #reset the game
            small = 1
            big = 100
            n = 1
    elif answer == "no":
        n = n +1            #To account how many times tries
        print("Is it larger than ", middle, "?(yes or no)")
        choice = input()
        if choice == "yes": #the user's number is larger than the guess number
            small = middle + 1
        else:               #the user's number is smaller than the guess number
            big = middle - 1


