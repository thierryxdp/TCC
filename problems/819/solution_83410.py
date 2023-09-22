def filtraMultiplos(lista, n):
    ''' função que recebe uma lista e um número, e retorna uma lista com todos os elementos divisíveis por N da lista original
    list, int -> list
    '''
    filtra = []
    i = 0
    while i < len(lista):
         if lista[i] // n ==0:
            filtra.insert (i, lista[i])
         
         i = i + 1
    return filtra