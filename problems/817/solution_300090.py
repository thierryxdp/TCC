def maiores(lista, n):
    '''Retorna uma lista com todos elementos maiores que n,
    da uma dada (lista)
    list, int -> list'''
    
    lista.sort()
    if n in lista:
        return lista[lista.index(n)+1:]
    else:
        lista.append(n)
        lista.sort()
        return lista[lista.index(n)+1:]
    
def acima_da_media(lista):
    '''Retorna uma dada lista contendo apenas o valores acima da média
    list -> list'''
    return lista