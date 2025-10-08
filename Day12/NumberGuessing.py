from random import randint

EASY = 10
HARD = 5

def check_answer(user_guess, actual_answer, turns):
    """checks answer against guess, returns the number of turns remaining"""
    if user_guess > actual_answer:
        print("too high, try a bit lower")
        return turns - 1
    elif user_guess < actual_answer:
        print("too low, try a bit higher")
        return turns - 1
    else:
        print(f"you won, the answer was {actual_answer}")

def set_difficulty():
    level = input("choose a difficulty level, type 'easy' or 'hard': ")
    if level == "easy":
        return EASY
    else: 
        return HARD
    
def game():
    print("welcome to the num guesser")
    print("try to guess the number im thinking of")
    answer = randint(1, 100)
#   print(f"the answer is {answer}")

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attemps left")
        guess = int(input("make a guess: "))
        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("ran out of attempts, you lost")
            return
        elif guess != answer:
            print("try another num")
game()