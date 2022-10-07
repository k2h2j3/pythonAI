fd = open('C:/Users/USER/Desktop/sensor10.csv', 'r')

for line in fd.readlines()[1:]:
    total = 0
    data = line.split(',')
    for i in data[2:-1]:
        total += (float(i) if len(i) > 0 else 0)

    print(total)


fd.close()
