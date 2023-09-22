def filtra_pares (tuplas):
    ''' Função que retorna apenas elementos pares da tupla original; tupla->tuple'''
    pares=()
    if (tuplas[0]%2)==0:
        pares+=(tupla[0],)
    if (tuplas[1]%2==0):
        pares+=(tupla[1],)
    if (tuplas[2]%2==0): 
        pares+=(tupla[2],)
    if (tuplas[3]%2==0):
        pares+=(tupla[3],)
    return pares