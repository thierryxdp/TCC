def primo(n):
    c = 0
    i = 0
    while i <= n or c < 2:
        i = i + 1
        x = n % i
        if x == 0:
            c += 1
    if c <=2:
        return True 
    else:
        return False