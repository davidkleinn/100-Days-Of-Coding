import random
import HangmanAscii
import ListOfWords

lives = 6

word = random.choice(ListOfWords.wordList)

playing = True
correctGuesses = []

print("========== WELCOME TO THE HANGMAN GAME ==========")
while playing:
    guess = input("Guess a letter: ").lower()


    placeholder = ""
    for i in range(len(word)):
        placeholder += "_"
    print(placeholder)

    display = ""

    if guess in correctGuesses:
        print(f"you already choose '{guess}'")

    for letter in word:
        if letter == guess:
            display += letter
            correctGuesses.append(guess)
        elif letter in correctGuesses:
            display += letter
        else:
            display += "_"

    print("Word to guess:" + display)
    print(" ")
 
    if guess not in word:
        lives -= 1
        print(f"=== wrong guess ===")
        
        if lives == 0:
            playing = False
            print("========================= YOU LOST =========================")
            print(f"================= THE WORD WAS: {word} ======================")
    
    if "_" not in display:
        playing = False
        print("========================= YOU WON =========================")

    if lives >= 0 and playing == True:
        print(HangmanAscii.hangmanStages[lives])