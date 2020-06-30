age = 6

# Both sides have to be true
if age > 2 and age < 8:
	print('Pay child price.')

city = input('Where do you live?')

# One side has to be true
if city == 'Los Angeles' or city == 'San Francisco':
	print('You live in California')
else:
	print('You live somehwere else.')

age = int(input('How old are you?'))

# NOT negates the opposte of the operations. Which means all of that is true.
# Since 21, the original age prior to the input, is not in between 2 and 8 it becomes false
# OR becomes AND with the NOT operator. 
# Since 21 is NOT greater than 65 it is also false.
# But since NOT is involved, it becomes true. 
if not ((age >= 2 and age <= 8) or age >= 65):
	print('You pay $10 and are not a child or Senior')
else: 
	print('You won!')

x = 0
y = -1
(x or y) and (x - 1 == y) and (y + 1 == x)
# true 			true			true

# Is the following expression truthy or falsy?
x = 15
y = 0
x or y  # this expression
# true / false
# But, or just has to have one side be true.