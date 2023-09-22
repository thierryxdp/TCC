def maiores(lista,n):
    a = lista.sort()
    b = lista.reverse()
    if lista[:3]>n:
        return [lista(1),lista(2),lista(3)]