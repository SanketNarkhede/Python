
class SubElements:
    def __init__(self):
        self.array=[-5,5,0,-1,1]
    '''
    l= []
    tot = 0
    def sub(self):
        for num in l:
            if num += 0:
                print(num)

            else: 
                print('n not found')

print(subelements.sub((-25,15,10,7,8)))

    '''

    def addition(self,array, number):
        found = True
        for a in range(0, number-2): 
            for b in range(a+1, number-1): 
                for c in range(b+1, number): 
                    if (array[a] + array[b] + array[c] == 0): 
                        print(array[a], array[b], array[c]) 
                        found = True
      
              
        #if elements are not found
        if (found == False): 
            print(" not exist ") 

s = SubElements()
s.addition([-5,5,1,-1,0],5)



