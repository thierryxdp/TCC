# tuple -> tuple

def filtra_pares(tup):
    '''
    Receb uma tupla tup com 4 inteiros e retorna uma tupla par com apenas os elementos 
    pares de tup na mesma ordem
    '''
    par=()
    i=0
    if tup[0]%2==0:
        par[i]=tup[0]
        i=i+1
    if tup[1]%2==0:
        par[i]=tup[1]
        i=i+1
    if tup[2]%2==0:
        par[i]=tup[2]
        i=i+1
    if tup[3]%2==0:
        par[i]=tup[3]
        i=i+1
    return par