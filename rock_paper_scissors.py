import random
import time

def game():
	user_choice = raw_input("Rock (R), Paper (P), or Scissors (S)?: ")

	if user_choice == "R":
		user_choice = 1
	elif user_choice == "P":
		user_choice = 2
	elif user_choice == "S":
		user_choice = 3
	else:
		print("Invalid choice!")
		game()

	comp_choice = random.randint(1, 3)

	if user_choice == 1:
		if comp_choice == 2:
			print("You lose!")
			time.sleep(0.5)
			again()
		elif comp_choice == 3: 
			print("You win!")
			time.sleep(0.5)
			again()
		elif comp_choice == 1:
			print("Tie!")
			time.sleep(0.5)
			again()
	if user_choice == 2:
		if comp_choice == 2:
			print("Tie!")
			time.sleep(0.5)
			again()
		elif comp_choice == 3:
			print("You lose!")
			time.sleep(0.5)
			again()
		elif comp_choice == 1:
			print("You win!")
			time.sleep(0.5)
			again()
	if user_choice == 3:
		if comp_choice == 2:
			print("You win!")
			time.sleep(0.5)
			again()
		elif comp_choice == 3:
			print("Tie!")
			time.sleep(0.5)
			again()
		elif comp_choice == 1:
			print("You lose!")
			time.sleep(0.5)
			again()


def again():
	choice = raw_input("Would you like to play again? y/n: ")

	if choice == "y":
		game()
	elif choice == "n":
		print("Thanks for playing!")
		exit()
	else:
		print("Invalid input")
		again()

game()
