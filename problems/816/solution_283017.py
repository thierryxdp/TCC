def maiores(lista,n):
    lista.append(n)
    lista.sort()
    maior = len(lista)>n
    lista.filter(maiores,lista)
    return lista