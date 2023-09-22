def filtra_pares(x):
    '''
    funcao que ira receber uma tupla de 4 elementos 
    tendo que retornar apenas os elementos pares, na mesma
    ordem em que estavam
    '''
    lista=()
    if x[0]%2=0:
        lista = lista+(x[0])
    elif x[1]%2=0:
        lista = lista+(x[1])
    elif x[2]%2=0:
        lista = lista+(x[2])
    elif x[3]%2=0:
        lista = lista+(x[3])
        return lista