def filtra_pares(t):
    '''Recebe uma tupla de 4 números inteiros e retorna uma tupla com
    os números pares
    tupla->tupla'''
    f=()
    if t[0]%2==0:
        f=f+(t[0],)
    if t[1]%2==0:
        f=f+(t[1],)
    if t[2]%2==0:
        f=f+(t[2],)
    if t[3]%2==0:
        f=f+(t[3],)
    return f