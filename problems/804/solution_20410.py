def par(n):
    return n%2==0
def filtra_pares(t):
    '''Função que dada uma tupla com 4 elementos inteiros, retorna uma nova tupla só com os elementos pares da tupla original
       tuple->tuple'''
    x = 0
    if par(tup[0]):
        x = x +(tup[0],)
    if par(tup[1]):
        x = x+(tup[1],)
    if par(tup[2]):
        x = x+(tup[2],)
    if par(tup[3]):
        x = x+(tup[3],)
    return x