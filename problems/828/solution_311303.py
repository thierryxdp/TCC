def primo(n):
    lista=[]
    for c in range(1,n+1):
        if n%c==0:
            lista.append(c)
    if len(lista)==2:
        return True
    else:
        return lista