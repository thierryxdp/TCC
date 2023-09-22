#Start your python function here
def filtra_pares(t):
    '''
    Funcao que recebe uma tupla com quatro elementos inteiros e
    retorna uma nova tupla contendo apenas pares da tupla original,
    na mesma ordem em que se encontravam
    tupla -> tupla.
    '''
    a,b,c,d = t
    s= ()
    if a%2==0:
        s=s+(a,)
    if b%2==0:
        s=s+(b,)
    if c%2==0:
        s=s+(c,)
    if d%2==0:
        s=s+(d,)
    return s