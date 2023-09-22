def filtra_pares(a,b,c,d):
    '''retorna uma tupla com os elementos pares dentre
    os quatro inseridos'''
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