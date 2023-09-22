def filtra_pares(tupla)->tuple:
    '''Funcao que retorna tupla com apenas elementos
    pares'''
    final=()    
    if tupla[0]%2==0:
        final+=(tupla[0],)
    if tupla[1]%2==0:
        final+=(tupla[1],)
    if tupla[2]%2==0:
        final+=(tupla[2],)
    if tupla[3]%2==0:
        final+=(tupla[3],)
    return final