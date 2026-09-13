n = int(input())
matrix = []
top_sum = right_sum = left_sum = bottom_sum = 0

matrix.extend([input().split() for _ in range(n)])
for r in range(n):
    for c in range(n):
        if r < c:
            if r < n - 1 - c:
                top_sum += int(matrix[r][c])
            elif r > n - 1 - c:
                right_sum += int(matrix[r][c])
        elif r > c:
            if r > n - 1 - c:
                bottom_sum += int(matrix[r][c])
            elif r < n - 1 - c:
                left_sum += int(matrix[r][c])

print(f'''Верхняя четверть: {top_sum}
Правая четверть: {right_sum}
Нижняя четверть: {bottom_sum}
Левая четверть: {left_sum}''')
