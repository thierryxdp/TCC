#filtra_pares 

def filtra_pares(tupla):
    '''tupla->tupla'''
    saida=tuple()
    if tupla[0]%2==0:
        saida+=(tupla[0],)
    if tupla[1]%2==0:
        saida+=(tupla[1],)
    if tupla[2] % 2 == 0:
        saida += (tupla[2],)
    if tupla[3] % 2 == 0:
        saida += (tupla[3],)
    return saida