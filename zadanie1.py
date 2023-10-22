f = open('input1.txt')
st = f.readline().split()
l = list(st)
m = 1
for i in range(0, len(l)):
    m *= int(l[i])
print(m)

