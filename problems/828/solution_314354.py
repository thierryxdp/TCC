def primo(n):
    qtd=0
    lista=list(range(1,n+1))
    for i in lista:
        if n%lista[i-1]==0:
            qtd=qtd+1
    if qtd==2:
        return True
    else:
        return False