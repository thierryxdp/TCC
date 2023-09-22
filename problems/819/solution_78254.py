def filtraMultiplos(lista,n):
    '''
    Função que recebe uma lista de números e retorna outra lista
    contendo todos os elementos originais que
    forem divisíveis por n
    
    lista, float -> lista
    '''
    multiploN = []
    i = 0
    while i< len(lista):
        if lista[i] % n == 0:
            multiploN.append(lista[i])
    	i = i + 1
    return multiploN