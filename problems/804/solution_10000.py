def filtra_pares(t):
    '''a partir de uma tupla com 4 números, retorna a mesma somente com os elementos pares
    tupla-->tupla'''
    a=t[0]
    b=t[1]
    c=t[2]
    d=t[3]
    r=()
    if a%2==0:
        r=(a,)
    if b%2==0:
        r=r+(b,)
    if c%2==0:
        r=r+(c,)
    if d%2==0:
        r=r+(d,)
    return r