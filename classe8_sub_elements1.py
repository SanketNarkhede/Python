class SubElements:
    def __init__(self):
        self.array = [10,20,20,50,0]

    def addition(self,array, number):
        found = True
        for a in range(0, number-1): 
            for b in range(a+1, number): 
                if (array[a] + array[b]  == 50): 
                    print(array[a], array[b]) 
                    found = True
      
              
    #if elements are not found
        if (found == False): 
            print(" not exist ") 
#s = SubElements()
#s.addition([10,20,20,50,0],5)
''' 
array = [-25,75,10,20,20] 
n = len(array) 
addition(array, n) 
'''

print(SubElements().addition([10,20,20,50,0],5))