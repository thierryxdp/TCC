def maiores(lista,n):
    '''
    Funçao que recebe uma lista de numeros e um numero e retorna
    uma lista com os numeros maiores que esse numero
    list, int -> list
    '''
    list.insert(lista,0,n)
    list.sort(lista)
    del lista[0:list.index(lista,n)+1]
    return lista