def filtra_pares(x):
    '''Faça uma função que receba quatro elementos pares, int, int, int, int -> tupla'''
    par = []
    if x[0]%2==0:
        par.insert(0,x[0])
    if x[1]%2==0:
        par.insert(1,x[1])
    if x[2]%2==0:
        par.insert(2,x[2])
    if x[3]%2==0:
        par.insert(3,x[3])
    return tuple(par)