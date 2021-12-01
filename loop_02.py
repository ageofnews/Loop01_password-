

while True:
	print('Please setup your password: ')
	password = input('password: ')
	confirm = input('Confirm? Y/N')
	if confirm == 'Y':
		break


chances = 3
while chances > 0:	
	print('chances: ',chances,'/3')
	password_answer = input('Please enter the password, you have three chances:')

	if password_answer == password:
		
		print('confirmed password!')
		break
	else:
		chances = chances - 1 

if chances == 0:
	print('you dont have enough chances' )


