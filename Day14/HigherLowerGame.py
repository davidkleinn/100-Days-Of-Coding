from art import logo, vs
from game_data import data
import random

def get_random_account():
    """picks a random data from the data"""
    random.choice(data)

def format_data(account):
    """format the data into printable state"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
    """checks if the user's guess is right"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def game():
    """function that has all the game logic"""
    print(logo)
    score = 0
    should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while should_continue:
        account_a = account_a
        account_b = get_random_account()

        while account_a == account_b:
            account_b == get_random_account()

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Compare B: {format_data(account_b)}.")

        guess = input("who has more followers? type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_right = check_answer(guess, a_follower_count, b_follower_count)

        print(logo)

        if is_right:
            score += 1
            print(f"you're right, current score: {score}")
        else:
            should_continue = False
            print(f"wrong answer buddy, final score: {score}")

game()