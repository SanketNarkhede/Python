class String:
    def __init__(self):
        self.string = ''
    def get_string(self):
        self.string = input("Enter a string")

    def put_string(self):
        print(self.string.upper())

s = String()
s.get_string()
s.put_string()

