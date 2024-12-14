import random
import hangman_art
import hangman_words
# from hangman_words import word_list
# from hangman_art import stages, logo


lives = 6
print(hangman_art.logo[0])
chosen_word = random.choice(hangman_words.word_list)

placeholder = ""
word_lenght = len(chosen_word)

for position in range(word_lenght):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"You already have: {lives}/6")

    guess = input("Choose a letter: ").lower()
    if guess in correct_letters:
        print(f"You already enter this letter {guess}, try another")

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

    if guess not in correct_letters:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

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
            print(f"The word was {chosen_word}")
        print(f"lives = {lives}")

    elif "_" not in display:
        game_over = True
        print("********** You Win! **********")
