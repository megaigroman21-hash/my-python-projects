word = input() + ' запретил букву'
letter = []

for c in word:
    if c not in letter and c != ' ':
        letter.append(c) 

letter.sort()
cnt = 0

for c in letter:
    print(word, letter[cnt])

    word = word.replace(letter[cnt], '')
    word = " ".join(word.split())
    
    cnt += 1
