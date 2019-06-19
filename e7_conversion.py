number=input('Enter the number to convert: ')

c1=((float(number) * 1.8) + 32)
print('\nInitial temperature is: ' + str(number) + ' degree celsius')
print('Conversion of number from Celsius to farenheight is: ' + str(c1))

c2=((float(number) - 32) / 1.8) 
print('\nInitial temperature is: ' + str(number) + ' degree Farenheight')
print('Conversion of number from farenheight to celsius is: ' + str(c2))