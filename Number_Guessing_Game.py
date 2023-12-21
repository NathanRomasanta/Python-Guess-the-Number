import random

art = """
  ________                              ___________.__              _______               ___.                 
 /  _____/ __ __   ____   ______ ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ 
\    \_\  \  |  /\  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/                  \/     \/          \/            \/    \/     \/       
        """

# Variables
msy_number = random.randint(1, 100)

HARD_LIVES = 5
EASY_LIVES = 10

user_lives = 0

game_over = False


def guess_checker(x):
    global game_over
    global user_lives
    # Checks if the user guessed the number
    if msy_number == x:
        print("Congratulations you guessed the number!")
        game_over = True
    # Prints an output of higher or lower depending on the user's guesses
    else:
        if msy_number > x:
            print("Too Low.")
            user_lives = user_lives - 1
            print(f"You have {user_lives} attempts remaining to guess the number")

        else:
            print("Too High.")
            user_lives = user_lives - 1
            print(f"You have {user_lives} attempts remaining to guess the number")


# Start of code
print(art)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 - 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
    user_lives = EASY_LIVES
else:
    user_lives = HARD_LIVES

while not game_over:
    guess = int(input("Make a guess: "))
    guess_checker(guess)

    if user_lives == 0:
        game_over = True
        print(f"You have run out of guesses, the mystery number is {msy_number}")
        print("Thanks for playing")
