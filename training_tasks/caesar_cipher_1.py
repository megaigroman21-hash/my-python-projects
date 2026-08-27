text = input().split(' ')
EN_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
new_text = ''

for symbol in text:
    cnt = 0
    for c in symbol:
        if c.isalpha():
            cnt += 1

    for c in symbol:
        if c.lower() in EN_ALPHABET:

            index = EN_ALPHABET.find(c.lower())
            if c.isupper():
                new_text += EN_ALPHABET[(index + cnt) % 26].upper()
            else:
                new_text += EN_ALPHABET[(index + cnt) % 26]

        else:
            new_text += c

    new_text += ' '        

print(new_text)
