# This section accepts name and ID
First_name, Last_name, User_ID = input('Enter your first name, last name, and user ID: ').split()
Name = First_name + ' ' + Last_name
print('Name: ', Name)
print('User ID: ', User_ID)

# This section conduct some basic calculations
x, y = input('Please enter one integer and one decimal number: ').split()
x = int(x)
y = float(y)
Sum = x + y

# This section prints the output of the calculations
print('You entered the numbers:', x, y)
print('The sum of', x, '+', y, '=', Sum)
