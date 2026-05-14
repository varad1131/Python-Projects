import random

min_range = 1
max_range = 100
attempts_limit = 10
score = 0

print("Welcome to the Number Guessing Game!")

while True:
    # Generate random number
    generated_number = random.randint(min_range, max_range)

    print(f"\nGuess the number between {min_range} and {max_range}")

    for attempt in range(1, attempts_limit + 1):
        user_guess = int(input(f"Attempt {attempt}: "))

        if user_guess == generated_number:
            print("Congratulations! You guessed the correct number.")
            score += 1
            break

        elif user_guess < generated_number:
            print("Too low! Try again.")

        else:
            print("Too high! Try again.")

        if attempt == attempts_limit:
            print(f"Sorry! The correct number was {generated_number}")

    play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("Your final score is:", score)
