def primo(n):
    
    for i in range(3, n):
        if n % i == 0:
            k = False
        else:
            k = True
    
    return k