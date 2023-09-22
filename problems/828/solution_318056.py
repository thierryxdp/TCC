def primo(n):
    r = []
    
    for i in list(range(1,n+1)):
        if n%i != 0:
            r.append(i)
    if len(r) == 2:
        return true