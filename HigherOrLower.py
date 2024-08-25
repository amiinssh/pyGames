import random

insta_personalities = {
    "Cristiano Ronaldo": ("Footballer", 600),
    "Kylie Jenner": ("Businesswoman", 380),
    "Lionel Messi": ("Footballer", 490),
    "Dwayne Johnson": ("Actor", 390),
    "Selena Gomez": ("Singer", 430),
    "Kim Kardashian": ("Businesswoman", 360),
    "Ariana Grande": ("Singer", 350),
    "Beyoncé": ("Singer", 320),
    "Justin Bieber": ("Singer", 290),
    "Taylor Swift": ("Singer", 270),
    "Neymar Jr.": ("Footballer", 210),
    "Kendall Jenner": ("Model", 260),
    "Jennifer Lopez": ("Singer", 240),
    "Nicki Minaj": ("Rapper", 220),
    "Khloé Kardashian": ("Reality TV Star", 230),
    "Miley Cyrus": ("Singer", 210),
    "Kourtney Kardashian": ("Reality TV Star", 210),
    "Kevin Hart": ("Comedian", 150),
    "Cardi B": ("Rapper", 160),
    "LeBron James": ("Basketball Player", 160),
    "Billie Eilish": ("Singer", 110),
    "Shakira": ("Singer", 110),
    "Gigi Hadid": ("Model", 100),
    "Zendaya": ("Actress", 190),
    "Tom Holland": ("Actor", 90),
    "Chris Hemsworth": ("Actor", 120),
    "Priyanka Chopra": ("Actress", 90),
    "Virat Kohli": ("Cricketer", 170),
    "Gal Gadot": ("Actress", 110),
    "Will Smith": ("Actor", 120),
    "Dua Lipa": ("Singer", 110),
    "David Beckham": ("Footballer", 90),
    "Vin Diesel": ("Actor", 90),
    "Shawn Mendes": ("Singer", 70),
    "Rihanna": ("Singer", 150),
    "Ellen DeGeneres": ("TV Host", 130),
    "Drake": ("Rapper", 140),
    "Snoop Dogg": ("Rapper", 100),
    "Katy Perry": ("Singer", 110),
    "Zendaya": ("Actress", 190),
}


def guessing():
    first_item, second_item = random.sample(list(insta_personalities.items()), 2)

    print(
        f"Compare A: {first_item[0]}, a {first_item[1][0]} with {first_item[1][1]} million followers."
    )
    print("vs")
    print(
        f"Compare B: {second_item[0]}, a {second_item[1][0]} with {second_item[1][1]} million followers."
    )

    while True:
        user_input = input("Who has more followers? Type 'A' or 'B': ").strip().upper()
        if user_input in ["A", "B"]:
            return user_input, first_item, second_item
        else:
            print("Invalid input. Please type 'A' or 'B'.")


def game():
    score = 0
    user_input, first_item, second_item = guessing()

    if (user_input == "A" and first_item[1][1] > second_item[1][1]) or (
        user_input == "B" and second_item[1][1] > first_item[1][1]
    ):
        score += 1
        print("Correct! You guessed it right.")
    else:
        print("Wrong! Game Over.")
        print(f"Your final score is: {score}")
        return

    print(f"Your score is: {score}")
    game()


game()
