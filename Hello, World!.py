from random import randint

def choiceElaborater(choice):
	if choice == 'r':
		return 'Rock'
	elif choice == 'p':
		return 'Paper'
	else:
		return 'Scissors';

def rockPaperScissors():
	global wins, losses, draws

	player = input('Rock (r), paper (p), or scissors (s)? ')

	while player != 'r' and player != 'p' and player != 's':
		player = input('Incorrect input. Rock (r), paper (p), or scissors (s)? ')

	chosen = randint(1,3)

	if chosen == 1: 
		computer = 'r'
	elif chosen == 2:
		computer = 'p'
	else:
		computer = 's'

	print()
	print('You\'ve chosen...', choiceElaborater(player), '!')
	print('Your opponent has chosen...', choiceElaborater(computer), end='! ')

	if player == computer:
		print('Draw!!')
		draws += 1
	else:
		if player == 'r' and computer == 's':
			print('You win!')
			wins += 1
		elif player == 'r' and computer == 'p':
			print('You lose!')
			losses += 1
		elif player == 's' and computer == 'p':
			print('You win!')			
			wins += 1
		elif player == 's' and computer == 'r':
			print('You lose!')
			losses += 1
		elif player == 'p' and computer == 'r':
			print('You win!')
			wins += 1
		elif player == 'p' and computer == 's':
			print('You lose!')
			losses += 1

	print()
	return;

wins = 0
losses = 0
draws = 0

print()
print("Welcome to Rock, Paper, Scissors!")
print()

while True:
	rockPaperScissors()

	playAgain = input('Play again? (y or n) ')

	while playAgain != 'y' and playAgain != 'n':
		playAgain = input('Incorrect input. Play again? (y or n) ')

	if playAgain == 'n':
		print()
		print('Total wins:', wins)
		print('Total losses:', losses)
		print('Total draws:', draws)
		print()
		break



