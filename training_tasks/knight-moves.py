chess_s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
chess_n = ['8', '7', '6', '5', '4', '3', '2', '1']

matrix = [['.'] * 8 for _ in range(8)]
n = list(input())

index_chess_s = chess_s.index(n[0])
index_chess_n = chess_n.index(n[1])
matrix[index_chess_n][index_chess_s] = 'N'

for i in range(-2, 3):
    for j in range(-2, 3):
        if abs(i) + abs(j) == 3:
            r = index_chess_n + j
            c = index_chess_s + i
            if 0 <= r <= 7 and 0 <= c <= 7:
                matrix[r][c] = '*'

for row in matrix:
    print(*row)
