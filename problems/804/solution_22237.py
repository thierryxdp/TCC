def filtra_pares (tuplas):
    ''' Função que retorna apenas elementos pares da tupla original; tupla->tuple'''
    pares=()
    if (tupla[0]%2)==0:
        pares+=(tupla[0],)
    if (tupla[1]%2==0):
        pares+=(tupla[1],)
    if (tupla[2]%2==0): 
        pares+=(tupla[2],)
    if (tupla[3]%2==0):
        pares+=(tupla[3],)
    return pares