def filtra_pares(x):
    '''dado uma tupla com 4 numeros inteiros essa funcao 
    nos devolve apenas os numeros pares; isso sem mudar a
    ordem dos teromos'''
    tup=()
    if x[0]%2==0:
        tup=tup+(x[0],)
    if x[1]%2==0:
        tup=tup+(x[1],)
    if x[2]%2==0:
        tup=tup+(x[2],)
    if x[3]%2==0:
        tup=tup+(x[3],)
    return tup#Start your python function here