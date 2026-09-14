n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
summer_2 = summer_3 = 0
flag = True

all_numbers = []
for row in matrix:
    for num in row:
        all_numbers.append(num)

for i in range(1, n ** 2 + 1):
    if i not in all_numbers:
        flag = False

total = sum(matrix[0])
for i in range(n):
    summer_2 += matrix[i][i]
    summer_3 += matrix[i][n - 1 - i]
    summer = sum(matrix[i])
    summer_1 = sum(matrix[row][i] for row in range(n))
    if flag == False:
        break

    if summer != total or summer_1 != total:
        flag = False

if summer_2 != total or summer_3 != total:
    flag = False

if flag:
    print('YES')
if not flag:
    print('NO')
