def filtraMultiplos(lista_num, n):
    ''' função que recebe uma lista e um número, e retorna uma lista com todos os elementos divisíveis por N da lista original
    list, int -> list
    '''
    filtra = []
    i = 0
    while i < len(lista_num):
         if lista_num[i] // n == 0:
            multiplos.insert( i, 0, lista[i])
            i = i + 1
    return filtra