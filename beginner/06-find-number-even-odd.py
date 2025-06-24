class FindEvenOdd:
    def __init__(self, number):
        self.number = number

    def find_even_odd(self):
        if self.number%2 == 0:
            print(f"{self.number} is EVEN")
        else:
            print(f"{self.number} is ODD")


obj = FindEvenOdd(16)
obj.find_even_odd()