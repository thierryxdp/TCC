def primo(p):
    r = int(p**(1/2))
    i = 2
    
    while i <= r:
        if p//i != 0:
            result = False
        i = i + 1
        else:
            result = True
    return result