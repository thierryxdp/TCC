def filtra_pares(tupla):
    ''' Função que retorna uma nova tupla contendo apenas os elementos pares da tupla original, dada como entrada uma tupla de quatro elementos.'''
    a,b,c,d=tupla
    t=()
    if a%2==0:
        t=t+(a,)
    if b%2==0:
        t=t+(b,)
    if c%2==0:
        t=t+(c,)
    if d%2==0:
        t=t+(d,)
    return t