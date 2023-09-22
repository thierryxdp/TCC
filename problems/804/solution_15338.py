def filtra_pares(tup):
    '''recebe uma tupla de quatro elementos inteiros e 
    retorna uma nova tupla apenas com os elementos pares
    tuple->tuple'''
    tupla=()
    if par(tup[0])==0:
        tupla=tupla+(tup[0],)
    if par(tup[1])==0:
        tupla=tupla+(tup[1],)
    if par(tup[2])==0:
        tupla=tupla+(tup[2],)
    if par(tup[3])==0:
        tupla=tupla+(tup[3],)
    return tupla
    
def par(x):
    '''retorna zero se o elemento x for par e um se for impar
    int->int'''
    if (x%2)==0:
        return 0
    else:
        return 1