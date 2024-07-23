import random

stages = ['''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives = 6

words = [
    "apple", "balloon", "camera", "dinosaur", "elephant", "forest", "galaxy", "harbor", "island", "jacket",
    "kangaroo", "lantern", "mountain", "notebook", "ocean", "panda", "quiver", "rocket", "sunset", "tiger",
    "umbrella", "volcano", "wizard", "yacht", "zebra", "anchor", "bridge", "castle", "diamond", "engine",
    "fountain", "glacier", "horizon", "igloo", "jungle", "kitten", "labyrinth", "meteor", "nebula", "orchid",
    "penguin", "quartz", "rainbow", "satellite", "treasure", "unicorn", "violet", "waterfall", "xylophone", "yeti",
    "avocado", "breeze", "canyon", "desert", "emerald", "firefly", "geyser", "hammock", "iceberg", "journey",
    "koala", "lemonade", "meadow", "nectar", "oasis", "peacock", "quaky", "reef", "sapphire", "thunder",
    "utopia", "valley", "whisper", "xenon", "yoga", "zodiac", "asteroid", "basil", "cactus", "drizzle", "eclipse",
    "fjord", "giraffe", "harvest", "illusion", "jewel", "kettle", "lightning", "mosaic", "nebula", "oyster",
    "phoenix", "quasar", "ripple", "starlight", "tidal", "universe", "vortex", "wanderlust", "xenolith", "zenith"
]

chosen_word = random.choice(words)

display = ["_" for _ in chosen_word]

guessed_letters = []

while "_" in display and lives > 0:
    print(stages[6 - lives])  
    print(" ".join(display))  
    
    guess = input("Guess a letter: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    if guess in guessed_letters:
        print("You have already guessed that letter.")
        continue
    
    guessed_letters.append(guess)
    
    if guess in chosen_word:
        for index in range(len(chosen_word)):
            if chosen_word[index] == guess:
                display[index] = guess
    else:
        lives -= 1
    
    if "_" not in display:
        print("Congratulations! You've guessed the word.")
    elif lives == 0:
        print(stages[6 - lives])  
        print("You lose! The word was:", chosen_word)

print(f"The chosen word was: {chosen_word}")
