import random

a = []

for i in range(100):
    a.append(random.randrange(1, 100))

a.sort()

print(a[0],a[99])

