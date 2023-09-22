def filtra_pares (tupla):
    '''função que retorna uma tupla nova que contém apenas os elementos
    pares da tupla original, ou seja, que filtre a (tupla) de entrada e
    retorne uma tupla com seus pares;
    tupla->tupla'''
    t = int((len(tupla))/2)
    return (tupla[::t])