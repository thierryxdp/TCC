def filtra_pares(t):
    '''recebe uma tupla t e retorna outra tupla com apenas os numeros pares de t; tup -> tup'''
    tt=()
    if t[0]%2==0:
        tt = tt + (t[0],)
    if t[1]%2==0:
        tt = tt + (t[1],)
    if t[2]%2==0:
        tt = tt + (t[2],)
    if t[3]%2==0: 
        tt = tt + (t[3],)
        return tt