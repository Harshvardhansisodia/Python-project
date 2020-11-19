def anna():
    import random
    total_guess = 0
    number = random.randrange(1, 10)
    print("Note you have only '6' chances!")
    while total_guess < 6:
        print("-Guess a no. between 1 to 10")
        guess = int(input())
        total_guess = total_guess + 1
        if number > guess:
            print("Your guess is too low, Try again")
        elif number < guess:
            print("Your guess is too high, Try again")
        else:
            print("You guess the correct number")
            break
        if total_guess == 6:
            print("You ran out of guess:")
    again=input("Do u want to restart the game: print 'yes'")
    if again=="yes":
        anna()
    else:
        exit()
anna()



