# print('ROCK')
# print('PAPER')
# print('SCISSORS')

# player_one = input('Do you pick rock, paper, or scissors?')
# player_two = input('Do you pick rock, paper, or scissors?')

# if player_one == 'rock' and player_two == 'scissors':
# 	print('Player One wins')
# elif player_one == 'rock' and player_two == 'paper':
# 	print('Player Two wins')
# elif player_one == 'paper' and player_two == 'rock':
# 	print('Player One wins')
# elif player_one == 'paper' and player_two == 'scissors':
# 	print('Player Two wins')
# elif player_one == 'scissors' and player_two == 'rock':
# 	print('Player Two wins')
# elif player_one == 'scissors' and player_two == 'paper':
# 	print('Player One wins')
# elif player_one == player_two:
# 	print('It is a tie!')
# else: 
# 	print('An error has occured.')

# REFACTORED
print('ROCK')
print('PAPER')
print('SCISSORS')

player_one = input('Player one, do you pick rock, paper, or scissors?')
print('NO CHEATING\n\n' * 20)
player_two = input('Player two, do you pick rock, paper, or scissors?')

if player_one == player_two:
	print('It is a tie!')
elif player_one == 'rock':
	if player_two == 'scissors':
		print('Player One wins')
	elif player_two == 'paper':
		print('Player Two wins')
elif player_one == 'paper':
	if player_two == 'rock':
		print('Player One wins')
	elif player_two == 'scissors':
		print('Player Two wins')
elif player_one == 'scissors':
	if player_two == 'paper':
		print('Player One wins')
	elif player_two == 'rock':
		print('Player Two wins')
else:
	print('Something went wrong')
