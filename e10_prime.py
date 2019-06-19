number=int(input('Enter a number: '))
if number > 1:

    for i in range(2, number//2):
        if(number % i) ==0:
            print(number,'Number is not prime.')
            break
    else:
        print(number ,'Number is  prime.')
        
else:
    print(number ,'Number is not prime.')


