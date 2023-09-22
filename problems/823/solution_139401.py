def faltante(L):
    list.sort(L)
    fim=len(L)
    cont=0 
    while cont<=fim:
        if L[cont]==(L[cont+1])-2:
            cont=cont+1
    return (L[cont])-1