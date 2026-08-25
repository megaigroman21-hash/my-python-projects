def is_valid_password(password):
    password = password.split(':')
    if len(password) != 3:
        return False
        
    if password[0] != password[0][::-1]:
        return False

    b = int(password[1])
    if b == 1:
        return False
    for i in range(2, b):
        if b % i == 0:
            return False
            
    c = int(password[2])     
    if c % 2 != 0:
        return False

    return True


psw = input()
print(is_valid_password(psw))
