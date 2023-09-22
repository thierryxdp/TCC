def filtraMultiplos (lista, n):
    '''essa funçao recebe uma lista e retorna uma segunda lista com apenas os elementos da
    lista original que sao multiplos de n
    list, int -> list'''
    i=1
    lista_mult = []
    
    while i < len(lista):
        if lista[i]/n == 0:
            list.append(lista_mult, lista[i])
            i=i+1
    return lista_mult