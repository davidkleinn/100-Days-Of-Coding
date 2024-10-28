from auctionLogo import logo
import os

moreBids = True

print(logo)

while moreBids:
    print("========== WELCOME TO THE SECRET AUCTION ==========")
    print(" ")
    name = input("what is your name?: ")
    price = int(input("what is your bid?: $"))

    bids = {}

    bids[name] = price

    highestBid = 0



    for name, price in bids.items():
        highestBid = price

        if price > highestBid:
            highestBid = price

    loop = input("is there any other bids? Type 'yes' or 'no'\n").lower()
    

    if loop == "no":
        moreBids = False
    elif loop == "yes":
        os.system('cls')

print(f"the highest bid was: ${highestBid}")
