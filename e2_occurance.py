String=input('Enter a string: ')

length=len(String)
print(length)


freq= {}

for i in String:
    if i in freq:
        freq[i]  += 1

    else:
        freq[i] =1

print('Occurance of letters are: ' + str(freq))

