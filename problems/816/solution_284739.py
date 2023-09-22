def maiores (lista,n):
    '''
    funçao que dados uma lista e um numero inteiro n, retorna 
    uma lista com os numeros maiores que n contidos na lista.
    list, int -> list
    '''
    lista2 = [n]
    lista3 = lista+lista2
    list.sort(lista3)
    numero = int(lista3.index(n))
    return lista3[n:]