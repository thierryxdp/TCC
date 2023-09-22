def primo(p):
    i=2
    while i < p//2 + 1:
        if p%i==0:
            return False
        i=i+1
    return True