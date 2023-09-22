def primo(n):
    r = []
    
    for i in list(range(1,n+1)):
        if n%i == 0:
            r.append(i)
    return len(r) == 0