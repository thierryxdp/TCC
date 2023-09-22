def filtra_pares(tupla):
    '''a funcao recebe uma tupla que contém 4 valores e filtra a tupla devolvendo apenas índices pares '''
    tuplax=()
    if tupla[0]%2==0:
        tuplax= tuplax + (tupla[0],)
    if tupla[1]%2==0:
        tuplax=tuplax + (tupla[1],)
    if tupla[2]%2==0:
        tuplax=tuplax + (tupla[2],)
    if tupla[3]%2==0:
        tuplax=tuplax+(tupla[3],)
    return tuplax#Start your python function here