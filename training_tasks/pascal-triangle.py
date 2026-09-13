from math import factorial
n = int(input())
res = []
my_list = []
for i in range(n):
    for j in range(i + 1):
        res.append(int((factorial(i) / (factorial(j) * factorial(i - j)))))
    my_list.append(res)
    res = []

for li in my_list:
    print(*li)
