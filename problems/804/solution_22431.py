def filtra_pares(tup):
    '''Funcao que retorna os elementos pares nas tuplas tupla->tupla'''
    pares=()
    if (tup[0]%2)==0:
    pares+=(tup[0],)
    if (tup[1]%2==0):
    pares+=(tup[1],)
    if (tup[2]%2==0):
    pares+=(tup[2],)
    if (tup[3]%2==0):
    pares+=(tup[3],)
    return pares