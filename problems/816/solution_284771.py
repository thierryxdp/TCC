def maiores(lista_numero,n):
    new=[]
    start=0
    while start < len(lista_numero):
        if lista_numero[start] > n:
            new = new + [lista_numero[start],]
        start = start + 1
    list.sort(new)
    return new