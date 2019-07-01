def two( a, b ):
    if a> b:
        return a
    return b
def three( a,b,c ):
    return two( a, two( b,c) )
print("maximum number is: ")
print(three(3, 6, -5))


