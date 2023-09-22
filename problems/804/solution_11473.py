def filtra_pares(tupla: tuple) -> tuple:
    '''Recebe uma tupla de 4 elementos numéricos e retorna outra tupla apenas com os números 
    pares dessa tupla inserida'''
    retorno = ()
    if (tupla[0]%2 == 0):
        retorno +=  (tupla[0],)
    if (tupla[1]%2 == 0):
        retorno +=  (tupla[1],)
    if (tupla[2]%2 == 0):
        retorno +=  (tupla[2],)
    if (tupla[3]%2 == 0):
        retorno +=  (tupla[3],)
        
    return retorno