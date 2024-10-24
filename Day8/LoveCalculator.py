def calculate_love_score(name1, name2):

    nameSum = (name1 + name2).lower()

    contTrue = 0
    contTrue += nameSum.count('t')
    contTrue += nameSum.count('r')
    contTrue += nameSum.count('u')
    contTrue += nameSum.count('e')

    contLove = 0
    contLove += nameSum.count('l')
    contLove += nameSum.count('o')
    contLove += nameSum.count('v')
    contLove += nameSum.count('e')

    score = int(f"{contTrue}{contLove}")

    print(score)


calculate_love_score("Kanye West", "Kim Kardashian")
