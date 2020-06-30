# ask for age
# age = input('How old are you?')

# if age:
# 	age = int(age)
# 	#  18-21 wristband
# 	if age >= 18 and age < 21:
# 		print('You can enter, but you need a wristband.')
# 	# 21+ drink, normal entry
# 	elif age >= 21:
# 		print('You can enter and can drink.')
# 		# Too young, I am sorry
# 	else: 
# 		print('You cannot enter the concert. I am sorry')
# else:
# 	print('Please enter an age.')

age = input('How old are you?')

if age:
	age = int(age)
	#  18-21 wristband
	if age >= 21:
		print('You can enter and can drink.')
	# 21+ drink, normal entry
	elif age >= 18:
		print('You can enter, but you need a wristband.')
		# Too young, I am sorry
	else: 
		print('You cannot enter the concert. I am sorry')
else:
	print('Please enter an age.')


# 	# ask for age
# age = input('How old are you?')

# if age != "":
# 	#  18-21 wristband
# 	if int(age) >= 18 and int(age) < 21:
# 		print('You can enter, but you need a wristband.')
# 	# 21+ drink, normal entry
# 	elif int(age) >= 21:
# 		print('You can enter and can drink.')
# 		# Too young, I am sorry
# 	else: 
# 		print('You cannot enter the concert. I am sorry')
# else:
# 	print('Please enter an age.')