# Write some code that requests the user to input another capital city.
# Add that city to the list of cities in capitals. Then print the file to the screen.

user_input = input('Please enter a capital city:> ')

file = open ('Capitals.txt', 'a')
file.write('\n' + user_input)
file.close

file = open('Capitals.text', 'r')
print(file.read())
file.close

