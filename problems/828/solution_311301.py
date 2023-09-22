def primo(n):
    lista=[]
    for c in range(1,n+1):
        if c%2==0:
            lista.append(c)
        elif c%3==0:
            lista.append(c)
        elif c%5==0:
            lista.append(c)
        elif c%7==0:
            lista.append(c)
    if len(lista)==2:
        return True
    else:
        return False