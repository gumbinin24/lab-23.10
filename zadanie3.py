file = open('input3.txt', encoding='utf-8')
s = file.readlines()
file.close()

data = []
for i in s:
    data.append(i.strip())

myList = []
for line in data:
    myList.append(line.split())

data.clear()

myList.sort(key=lambda x: x[2])

for i in myList:
    data.append(' '.join(map(str, i)))
print(data)

f1 = open('youngest_kid.txt', 'w', encoding='utf-8')
f1.write(data[0])
f1.close()

f2 = open('oldest_kid.txt', 'w', encoding='utf-8')
f2.write(data[-1])
f2.close()
