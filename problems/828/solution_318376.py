def primo(p):
    r = int(p**(1/2))+1
    
    for n in range(r):
        if p%n == 0:
            return True