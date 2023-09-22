def filtra_pares(e1:int,e2:int,e3:int,e4:int)->tuple:
    '''Funcao que retorna tupla com apenas elementos
    pares'''
    final=()
    if e1%2==0:
        final+=(filtra_pares[0],)
    if e2[1]%2==0:
        final+=(filtra_pares[1],)
    if e3[2]%2==0:
        final+=(filtra_pares[2],)
    if e4[3]%2==0:
        final+=(filtra_pares[3],)
    return final