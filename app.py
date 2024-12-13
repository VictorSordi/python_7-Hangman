import random
import hangman_art
import hangman_words


lives = 6
print(hangman_art.logo[0])
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

placeholder = ""
word_lenght = len(chosen_word)

for position in range(word_lenght):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []
tries = []

while not game_over:
    guess = input("Choose a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print("Word to guess:" + display)
    print("\n")

    if tries == guess:
        print("You typed this letter already!")

    if guess not in chosen_word:
        lives -= 1
        if lives == 6:
            print(hangman_art.stages[6])
        elif lives == 5:
            print(hangman_art.stages[5])
        elif lives == 4:
            print(hangman_art.stages[4])
        elif lives == 3:
            print(hangman_art.stages[3])
        elif lives == 2:
            print(hangman_art.stages[2])
        elif lives == 1:
            print(hangman_art.stages[1])
        elif lives == 0:
            game_over = True
            print(hangman_art.stages[0])
            print("********** You Lose! **********")
        print(f"lives = {lives}")

    elif "_" not in display:
        game_over = True
        print("********** You Win! **********")
