def filtra_pares(tupla):
    '''retorna uma tupla apenas com os elementos pares da tupla "tup"'''
    '''tup-->tup'''
    if ((type((tupla[0])/2))==int):
        pares=(tupla[0],)
    if ((type((tupla[1])/2))==int):
        pares=pares+(tupla[1],)
    if ((type((tupla[2])/2))==int):
        pares=pares+(tupla[2],)
    if ((type((tupla[3])/2))==int):
        pares=pares+(tupla[3])
    return pares