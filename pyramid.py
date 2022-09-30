class Pyramid:
    #피라미드 생성
    def __init__(self, height):
        self.height = height
    # 높이값 수정
    def set(self, height):
        self.height = height
    # 생성된 피라미드 출력
    def show(self):
        for i in range(1, self.height+1):
            print(' ' * (self.height - i) + '*' * (i * 2 - 1))
    # 피라미드 블록 개수
    def getBlock(self):
        total = 0
        for i in range(1, self.height+1):
            total = total + (i * 2 - 1)
        return total

p = Pyramid(5)
p.show()