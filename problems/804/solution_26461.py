def filtra_pares(tupla):
    '''Função que recebe uma tupla com quatro elementos e retorna uma tupla contendo sos elementos pares desta'''
    pares = []
    for item in tupla:
        if(item %2 == 0):
            pares.append(item)
           
    return tuple(pares)