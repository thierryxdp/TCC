def maiores(lista, n):
    ''' função que retorna numeros da lista maiores que n
        list, int ---> list '''
    list.append(lista, n)
    list.sort(lista)
    a = list.index(lista, n)
    if a == 0:
        return lista[a+1:]
    if a == 1:
        return lista [a+1:]
    else:
        return lista[a+1:]
    
def acima_da_media(lista):
    ''' função que retorna notas acima da media '''
    list.sort(lista)
    return maiores(lista, 5)