def filtra_pares(a):
    '''separa os numeros pares da tupla inicial e retorna na ordem.
       tuple->tuple'''
    pares_novo=()
    if a[0]%2==0:
        pares_novo=pares_novo+(a[0],)
    if a[1]%2==0:
        pares_novo=pares_novo+(a[1],)
    if a[2]%2==0:
        pares_novo=pares_novo+(a[2],)
    if a[3]%2==0:
        pares_novo=pares_novo+(a[3],)
    return pares_novo