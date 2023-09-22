def maiores(lista,n):
    lista.append(n)
    lista.sort()
    lista_valida = len(lista)>n
    if len(lista) > n:
        return lista_valida
    else:
        return lista