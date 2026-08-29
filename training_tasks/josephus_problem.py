n, k = int(input()), int(input())
list = [i for i in range(1, n + 1)]

def pick(list, k):
    index = (k-1) % len(list)
    new_list = list[index + 1:] + list[:index] 

    return new_list


while len(list) != 1:
    list = pick(list, k)

print(*list)
