
a=[]
n=int(input('Enter number of elements: '))
for i in range(1,n+1):
    b=int(input('enter number: '))
    a.append(b)
a.sort()
print('largest element is: ' + str(a[n-1]) )

