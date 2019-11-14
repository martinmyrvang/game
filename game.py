import random

correct = random.randint(1, 10)

guess = input("Enter your guess: ")
guess = int(guess)

while guess != correct:
	if guess > correct:
		print("You've guessed too high. Try guessing lower.")
	else:
		print("You've guessed too low. Try guessing higher.")
	
	guess = int(input("Enter your guess: ")) 

print("Congratulations! You've guessed correctly.") 