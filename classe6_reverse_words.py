class Reverse:
    def reverse_words(self,s):
        self.string = s
        new= s.split()
        print(new)
        return ' '.join(reversed(s.split()))

#r = Reverse()
#r.reverse_words('sanket here')

print(Reverse().reverse_words('sanket here'))
