string=input('Enter a string:')
length=len(string)
print('Length of given string is: ' + str(length))

numbers= sum(count.isdigit() for count in string)
print('\nDigits: ' + str(numbers))

letters= sum(count.isalpha() for count in string)
print('\nletters: ' + str(letters))