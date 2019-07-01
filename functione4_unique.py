def unique_number(var):
    x = []
    for a in var:
        if a not in x:
            x.append(a)
    return x


  
print(unique_number([1,2,3,3,3,3,4,5])) 


