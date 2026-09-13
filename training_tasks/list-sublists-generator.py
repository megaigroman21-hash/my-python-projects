s = input().split()
row = [[]]
n = len(s)
for i in range(1, len(s) + 1):
    for j in range(n):
        row.append(s[j:j + i])
    n -= 1

print(row)
