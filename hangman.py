import random
import words
from Art import logo, stages

print(" Welcome to the Game ")
print(logo)

chosen_word = random.choice(words.WORDS)

print(chosen_word)
lives = 6

word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guess = input("Guess the word!  ").lower()

    if guess in display:
        print(f" you have already gussed  '{guess}'")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f" you gussed the letter {guess} that's not in the word")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(" you lose ")

        
    print(f"{''.join(display)}")   

    if "_" not in display:
        end_of_game = True
        print(" you win ")

    print(stages[lives])
    
        
