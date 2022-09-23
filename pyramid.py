def pyramid(num):
    for i in range(1, num + 1):
        result = ' ' * (num - i) + '*' * ((2 * i) - 1)
        print(result)

n = int(input('floor'))
pyramid(n)

