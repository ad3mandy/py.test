# This code shows how to use "" and some other special characters like / in a string
print()

# This sections accept name and ID
first_name, last_name, student_id = input("Please enter your first name, last name and user ID: ").split()
print()
print(first_name, last_name)
print(student_id)
print()

# This section is useful for writing signature words for cmd tools
print('''*********************
*                   *
*  1. World         *
*  2. Excel         *
*  3. Power Point   *
*  4. Paint         *
*                   *
*********************''')

print()

print('''Messi is the "God" of soccer.''')
print('To', '''access your file, go to H:\Python\Lab2.py''', sep=' ')
print("Hello Amanda!!! How are you", end='???')
print()
