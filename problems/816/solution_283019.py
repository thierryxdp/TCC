def maiores(lista,n):
    lista.append(n)
    lista.sort()
    maiores = len(lista)>n
    lista.filter(maiores,lista)
    return lista