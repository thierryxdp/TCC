def maiores(lista,n):
    if n not in lista:
        lista.append(n)
    lista.sort()
    a=lista.index(n)
    lista_2=lista[a+1:]
    b=lista_2.count(n)
    return lista_2[b:]