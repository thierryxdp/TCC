def filtraMultiplos(listaNum,n):
    '''Dado uma lista de números e um numero n, retorna uma lista com 
    os números dessa lista que são divisíveis por n'''
    i = 0
    listaMultiplos = []
    while (i < len(listaNum)):
    	if (listaNum[i] % n) == 0:
            list.append(listaMultiplos,listaNum[i])
        i = i + 1
        return listaMultiplos