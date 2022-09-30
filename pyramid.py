class Pyramid:
    def __init__(self, height):
        self.height = height
    def set(self, height):
        self.height = height
    def show(self):
        for i in range(1, self.height+1):
            print(' ' * (self.height - i) + '*' * (i * 2 - 1))

    def getBlock(self):
        total = 0
        for i in range(1, self.height+1):
            total = total + (i * 2 - 1)
        return total

p = Pyramid(5)
p.show()