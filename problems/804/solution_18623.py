# tuple -> tuple

def filtra_pares(tup):
    '''
    Receb uma tupla tup com 4 inteiros e retorna uma tupla par com apenas os elementos 
    pares de tup na mesma ordem
    '''
    par=[]
    if tup[0]%2==0:
        par=par+[tup[0]]
    if tup[1]%2==0:
        par=par+[tup[1]]
    if tup[2]%2==0:
        par=par+[tup[2]]
    if tup[3]%2==0:
        par=par+[tup[3]]
    retun par