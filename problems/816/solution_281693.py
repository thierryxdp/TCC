def maiores(lista,n):
    a = lista.sort()
    b = lista.reverse()
    c = list(n)
    if lista[:3]>n:
        return [lista(1),lista(2),lista(3)]