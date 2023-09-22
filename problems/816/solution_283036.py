def maiores(lista,n):
    lista.append(n)
    lista.sort()
    lista_valida = lista[i]>n
    if len(lista) > n:
        return lista_valida
    else:
        return lista