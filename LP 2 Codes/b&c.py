import random

n = 4;
number = random.sample(range(1,10), n)

guess_counter = 0


def guesser():

    koshish = int(input("\nGuess " + str(guess_counter) + ": "))
    guess = [i for i in str(koshish)]

    if len(guess) != n:
        print("Please enter a valid 4 digit number")
        guesser()
        return 0

    for i in range(n):
        for j in range(i+1, n):
            if guess[i] == guess[j]:
                print("Duplicates detected")
                guesser()
                return 0

    bulls = 0
    cows = 0
    cattle = 0

    for i in range(n):

        if str(number[i]) in guess:
            cattle += 1

    for i in range(n):
        
        if str(number[i]) == guess[i]:
            bulls += 1

    cows = cattle - bulls

    def printer():
        for i in range(n):
            print(guess[i], end=" ")

    printer()
    print("\t" +str(bulls) + " Bulls " + str(cows) + " Cows")

    return bulls


print("\nYou can start decoding now\n\n")
while(True):
    guess_counter += 1
    bulls = guesser()
    if bulls == n:
        break

print("You took " + str(guess_counter) + " guesses to decode!!!")