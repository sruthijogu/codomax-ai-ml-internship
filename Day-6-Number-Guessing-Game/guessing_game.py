import random
secret_number = random.randint(1,50)
print("Welcome to the number guessing game!")
print("I have chosen a number between 1 and 50. Can you guess it?")
attempts = 0
while True:
    guess = int(input("Guess the number:"))
    attempts = attempts+1
    if guess == secret_number:
        print("Correct! You guessed the number!")
        print("Number of attempts:", attempts)
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")