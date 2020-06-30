import random

print('ROCK')
print('PAPAER')
print('SCISSORS')

player = input('Do you pick rock, paper, or scissors?').lower()

rand_num = random.randint(0,2)

if rand_num == 0:
	computer = 'rock'
elif rand_num == 1:
	computer = 'paper'
else:
	computer = 'scissors'
print(f'Computer played {computer}')

if player == computer:
	print('It is a tie')
elif player == 'rock':
	if computer == 'scissors':
		print('Player wins')
	else:
		print('Computer wins')
elif player == 'paper':
	if computer == 'rock':
		print('Player wins')
	else:
		print('Computer wins')
elif player == 'scissors':
	if computer == 'paper':
		print('Player wins')
	else:
		print('Computer wins')
else:
	print('Please enter a move.')
