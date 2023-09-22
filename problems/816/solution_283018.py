def maiores(lista,n):
    lista.append(n)
    lista.sort()
    maior = len(lista)>n
    lista.filter(maior,lista)
    return lista