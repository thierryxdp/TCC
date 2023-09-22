def primo(num):
    q = 2
    i = 3
    if num % 2 == 0:
        q += 1
    while i < num:
        if num % i == 0:
            q += 1
        i += 2
    if q == 2:
        return True
    else:
        return False