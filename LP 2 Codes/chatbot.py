import random
 
def no_game():
    # Generate a random number between 1 and 100
    number = random.randint(1, 100)
 
    # Initialize the number of guesses
    guesses = 0
 
    # Keep looping until the user guesses the number
    while guesses < 10:
        # Get the user's guess
        guess = int(input("Guess a number between 1 and 100: "))
 
        # Check if the guess is correct
        if guess == number:
            print("Congratulations! You guessed the number correctly!")
            break
 
        # Otherwise, tell the user if their guess was too high or too low
        elif guess < number:
            print("Your guess was too low.")
        else:
            print("Your guess was too high.")
 
        # Increment the number of guesses
        guesses += 1
 
        # If the user runs out of guesses, tell them they lost
        if guesses == 5:
            print("Sorry, you ran out of guesses. The number was", number)
            chatbot()


def Rock_Paper_scissor():
    # print multiline instruction
    # perform string concatenation of strings
    print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
        + "Rock vs Paper -> Paper wins \n"
        + "Rock vs Scissors -> Rock wins \n"
        + "Paper vs Scissors -> Scissor wins \n")
 
    while True:
        print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
        # take the input from user
        choice = int(input("Enter your choice: "))    
        # OR is the short-circuit operator
        # if any one of the condition is true
        # then it returns True value
 
        # looping until user enters valid input
        while choice > 3 or choice < 1:
            choice = int(input('Enter a valid choice please: '))
 
        # initialize value of choice_name variable
        # corresponding to the choice value
        if choice == 1:
            choice_name = 'Rock'
        elif choice == 2:
            choice_name = 'Paper'
        else:
            choice_name = 'Scissors'
 
        # print user choice
        print('User choice is:', choice_name)
        print('Now it\'s Computer\'s Turn....')
 
        # Computer chooses randomly any number
        # among 1, 2, and 3. Using randint method
        # of random module
        comp_choice = random.randint(1, 3)
 
        # looping until comp_choice value
        # is equal to the choice value
        while comp_choice == choice:
            comp_choice = random.randint(1, 3)
 
        # initialize value of comp_choice_name
        # variable corresponding to the choice value
        if comp_choice == 1:
            comp_choice_name = 'Rock'
        elif comp_choice == 2:
            comp_choice_name = 'Paper'
        else:
            comp_choice_name = 'Scissors'
        print("Computer choice is:", comp_choice_name)
        print(choice_name, 'Vs', comp_choice_name)
        # we need to check for a draw
        if choice == comp_choice:
            print('It\'s a Draw', end="")
            result = "DRAW"
        # condition for winning  
        if (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1):
            print('Paper wins =>', end="")
            result = 'Paper'
        if (choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
            print('Rock wins =>', end="")
            result = 'Rock'
        if (choice == 2 and comp_choice == 3) or (choice == 3 and comp_choice == 2):
            print('Scissors wins =>', end="")
            result = 'Scissors'
        # Printing either user or computer wins or draw
        if result == 'DRAW':
            print("<== It's a tie ==>")
        elif result == choice_name:
            print("<== User wins ==>")
        else:
            print("<== Computer wins ==>")
        print("Do you want to play again? (Y/N)")
        # if user input n or N then condition is True
        ans = input().lower()
        if ans == 'n':
            break
    # after coming out of the while loop
    # we print thanks for playing
    print("Thanks for playing")
 
def greet(bot_name, birth_year):
    print("Hello! My name is {0}.".format(bot_name))
    print("I was created in {0}.".format(birth_year))
 
def remind_name():
    print('Please, remind me your name.')
    name = input()
    print("What a great name you have, {0}!".format(name))
 
def end():
    print('Congratulations, have a nice day!')
    print('.................................')
    print('.................................')
    print('.................................')
    input()
def chatbot():
    a= True
    while (a):
        print("Select the game you want to play :")
        print("1. Guessing the no. game")
        print("2. Stone Paper Scissor")
        print("3. exit")
        print("Enter your choose")
        argument=int(input())
 
        def switch_case(argument):
            if argument == 1:
                no_game()
            elif argument == 2:
                Rock_Paper_scissor()
            elif argument == 3:
                exit()
            else:
                return "Invalid choice"
   
        switch_case(argument)
greet('TE-Chatbot', '2022') # change it as you need
remind_name()
chatbot()
end()