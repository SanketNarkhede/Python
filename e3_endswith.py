string= input('Enter string: ')
var='ing'
if(string.endswith(var)):
    print('Newly added string  is: ' + str(string) + 'ly')
elif(len(string)>=3):
    print('Newly added string is: ' +str(string) + 'ing')
else:
    print('Please enter a string having length greater than three')
    print('String is: ' +str(string))

