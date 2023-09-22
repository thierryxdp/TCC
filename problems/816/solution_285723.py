def maiores(lista, n):
    ''' função que retorna numeros da lista maiores que n
        list, int ---> list '''
    list.append(lista, n)
    list.sort(lista, reverse=True)
    a = list.index(lista, n)
    if a == 0:
        return list.reverse(lista[0:0])
    if a == 1:
        return list.reverse(lista[0:1])
    else:
        return list.reverse(lista[0:a])