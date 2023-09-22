def filtra_pares(x):
    '''funcao que recebe uma tupla como entrada e filtra os elementos pares,e retorna uma nova tupla apenas com essses elemtnos paress;
    tuple -> tuple'''
    tupla = ()
    if x[0]%2==0:
        tupla = tupla +(x[0],)
    elif x[1]%2==0:
        tupla = tupla +(x[1],)
    elif x[2]%2==0:
        tupla = tupla +(x[2],)
    elif x[3]%2==0:
        tupla = tupla+(x[3],)
    else:
        return tupla