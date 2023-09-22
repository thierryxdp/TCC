def maiores (lista_numeros, n):
    '''Função retorna todos os numeros maiores que n entre os numeros da lista dada.
    list, int -> list'''
    list.append (lista_numeros,n)
    list.sort (lista_numeros)
    posição = list.index (lista_numeros, n)
    return lista_numeros[posição+1:]