from random import randint

easy_level_turns = 10
hard_level_turns = 5

# function to check user's guess against actual answer

def check_answer(guess, answer,turns):
    if guess > answer:
        print("Too high!")
        return turns-1
    elif guess < answer:
        print("Too low!")
        return turns-1
    else:
        print(f"You got it!The answer is {answer}")

# make a function to set difficulty

def set_difficult():
    level = input("Choose a difficulty leve. Type 'easy' or'hard': ")
    if level == "easy":
        return easy_level_turns
    else:
        return hard_level_turns

def game():
    print("welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1,100)
    turns = set_difficult()
    guess =0
    while guess != answer:
        print(f"You have {turns} attempt remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You;ve run out of guesses , you lose.")
            return
        elif guess!= answer:
            print("Guess again.")


game()
