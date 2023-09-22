def filtra_pares(x):
    '''Função que retorna quatro elementos pares, int, int, int, int -> int, int, int, int'''
    par()
    if x[0]%2==0:
        par=par+(x[0],)
    if x[1]%2==0:
        par=par+(x[1],)
    if x[2]%2==0:
        par=par+(x[2],)
    if x[3]%2==0:
        par=par+(x[3],)
    return par