def par(n):
    return n%2==0
def filtra_pares(t):
    '''Função que dada uma tupla com 4 elementos inteiros, retorna uma nova tupla só com os elementos pares da tupla original
       tuple->tuple'''
    x = 0
    if par(t[0]):
        x = x +(t[0],)
    if par(t[1]):
        x = x+(t[1],)
    if par(t[2]):
        x = x+(t[2],)
    if par(t[3]):
        x = x+(t[3],)
    return x