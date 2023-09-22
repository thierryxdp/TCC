def maiores(lista, n):
    ''' função que retorna numeros da lista maiores que n
        list, int ---> list '''
    list.append(lista, n)
    list.sort(lista)
    a = list.index(lista, n)
    if a == 0:
        return lista[a:]
    if a == 1:
        return lista [a+1:]
    else:
        return lista[a+1:]