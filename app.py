import random

stages = ['''
 _______
 |/    |
 |    (_)
 |    \|/
 |    / \
 |
_|___
======
''', '''
 _______
 |/    |
 |    (_)
 |    \|/
 |    /
 |
_|___
======
''', '''
 _______
 |/    |
 |    (_)
 |    \|/
 |
 |
_|___
======
''', '''
 _______
 |/    |
 |    (_)
 |    \|
 |
 |
_|___
======
''', '''
 _______
 |/    |
 |    (_)
 |    \
 |
 |
_|___
======
''', '''
 _______
 |/    |
 |    (_)
 |
 |
 |
_|___
======
''', '''
 _______
 |/    |
 |
 |
 |
 |
_|___
======
''']

word_list = ["aardvark", "baboon", "camel", "apple"]

lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_lenght = len(chosen_word)

for position in range(word_lenght):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []


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
    print(display)
    print("\n")

    if guess not in chosen_word:
        lives -= 1
        if lives == 6:
            print(stages[6])
        elif lives == 5:
            print(stages[5])
        elif lives == 4:
            print(stages[4])
        elif lives == 3:
            print(stages[3])
        elif lives == 2:
            print(stages[2])
        elif lives == 1:
            print(stages[1])
        elif lives == 0:
            game_over = True
            print(stages[0])
            print("You Loose")
        print(f"lives = {lives}")

    elif "_" not in display:
        game_over = True
        print("You Win!")
