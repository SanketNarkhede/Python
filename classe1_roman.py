class Roman:
    def to_Roman(self, num):
        
        val = [
            1000, 900, 500, 400,100, 90, 50, 40,10, 9, 5, 4,1
            ]
        symbol = [
            "M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"
            ]
        roman_number = ''
        i = 0
        #number = int(input('Enter a number'))
        while  num > 0:
            for num in range(num // val[i]):
                roman_number += symbol[i]
                num -= val[i]
            i += 1
        return roman_number


print(Roman().to_Roman(1))
print(Roman().to_Roman(121))
