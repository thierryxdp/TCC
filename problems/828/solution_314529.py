def primo(n):
    d = int(n/2)    
    res = True
    while res and d > 1:
        if  n%d == 0:
            res = False
        d = d -1
    return res