def faltante(lista):
    """ Essa função recebe uma lista de tamanho N -1 e 
    retorna o número faltante dessa lista. list-> int"""
    i = 0 
    while i < len(lista):
        novalista = list(range(lista[-1]))
        if lista[:] != novalista[:]:
            i = i+1
        i = i+1
    return novalista