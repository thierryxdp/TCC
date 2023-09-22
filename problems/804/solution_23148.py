def filtra_pares(t):
    '''recebe uma tupla t e retorna outra tupla com apenas os numeros pares de t; tup -> tup'''
    tt=()
    if int(t[0])%2==0:
        tt = tt + (t[0],)
    if int(t[1])%2==0:
        tt = tt + (t[1],)
    if int(t[2])%2==0:
        tt = tt + (t[2],)
    if int(t[3])%2==0: 
        tt = tt + (t[3],)
    else:
        tt=tt
        return tt