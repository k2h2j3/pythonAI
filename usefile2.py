fd = open('C:/Users/USER/Desktop/sensor10.csv', 'r')

lst = []


for line in fd.readlines()[1:]:
    data = line.split(',')
    tmp = []
    for i in data[2:-1]:
        tmp.append((float(i) if len(i) > 0 else 0))
    lst.append(tmp)


#print(len(lst), len(lst[0]))
#print(lst[0][0])
colsum = []
for col in range(len(lst[0])):
    total = 0
    for row in range(len(lst)):
        total += lst[row][col]

    colsum.append(total)

print(colsum)
fd.close()