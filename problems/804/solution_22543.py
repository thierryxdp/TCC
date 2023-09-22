def filtra_pares(tupla):
    '''Seleciona os elementos pares de uma tupla, retornando-os em outra tupla'''
    pares=()
    if tupla[0]%2==0:
        pares=pares+tupla[0]
    if tupla[1]%2==0:
        pares=pares+tupla[1]
    if tupla[2]%2==0:
        pares=pares+tupla[2]
    if tupla[3]%2==0:
        pares=pares+tupla[3]
    return pares