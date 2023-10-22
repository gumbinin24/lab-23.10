with open('input2.txt', 'r') as f:
    lines = [line.strip() for line in f]

result = list(map(int, lines))
result.sort()
res = list(map(str, result))

with open('out.txt', 'w') as f:
    f.writelines(f"{item}\n" for item in res)
