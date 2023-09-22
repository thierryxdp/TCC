def filtra_pares(x):
    '''Recebe uma tupla x com quatro elementos inteiros e retorna
    uma nova tupla contendo apenas os elementos pares da original. 
    tuple-> tuple'''
    y=()
    if x[0]%2==0:
        y = y + (x[0],)
    if x[1]%2==0:
        y+= (x[1],)
    if x[2]%2==0:
        y+= (x[2],)
    if x[3]%2==0:
        y+= (x[3],)
    return y