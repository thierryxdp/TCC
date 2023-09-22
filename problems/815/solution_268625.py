def insere(lista,n):
    a=list.index(lista,n)
    if a<n:
        return list.insert(lista,n,a+1)
    if a>n:
        return list.insert(lista,n,a+1)