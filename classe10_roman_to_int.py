class toInt:
    def __init__(self):

        self.values = (('M',  1000),('CM', 900),('D',  500),('CD', 400),('C',  100),('XC', 90),('L',  50),('XL', 40),('X',  10),('IX', 9),('V',  5),('IV', 4),('I',  1))

    def RomanToInt(self,string):
        result = 0
        array = []
        for i in range(len(string)):
            for letter, value in self.values:
                if string[i] == letter:
                    array.append(value)
        array.append(0)
        for i in range(len(string)):
            if array[i] >= array[i+1]:
                result = result + array[i]
            else:
                result = result - array[i]
        return result


print(toInt().RomanToInt('XI'))

