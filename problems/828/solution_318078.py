def primo(n):
    
    res = False
    while i < n and not res:
        x = n % i
        if x == 0:
            res = True
            i += 1
        if res:
            return False
        else:
             return True