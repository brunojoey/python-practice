# x == '\U0001f600'

for x in range(1,11):
	print('\U0001f600' * x)

times = 1
while times <= 10:
	print('\U0001f600' * times)
	times += 1

# without string multiplication
for x in range(1,11):
	count = 1
	emoji = ''
	while count < x:
		emoji += '\U0001f600'
		count += 1
	print(emoji)

