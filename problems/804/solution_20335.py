def filtra_pares(T):
    '''Identifica os elementos pares da tupla 'T' e retorna uma tuplacom os mesmos em suas respectivas ordens;
tuple -> tuple'''
    Tf = ()
    if T[0]%2==0:
        Tf = Tf + (T[0],
    if T[1]%2==0:
        Tf=Tf+(T[1],)
    if T[2]%2 == 0:
        Tf = Tf + (T[2],)
    if T[3]%2 == 0:
        Tf = Tf + (T[3],)
    return Tf