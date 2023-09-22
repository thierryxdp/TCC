def primo(n):
    i = 0
    res = False
    while i < n and not res:
        i = i + 1
        x = n % i
        if x == 0:
            res = True
            i += 1
        if res:
            return False
        else:
             return True