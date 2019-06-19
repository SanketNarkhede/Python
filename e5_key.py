dict={"a":"1", "b": "2"}
print(dict)

new=input('Add new key: ')
for i in dict:
    if(new == dict[i] ):
        print('Key already exist')
        print('You cannot add this key ')
    
    else:
        print('No key matching..You can add this key')
    
