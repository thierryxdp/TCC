def filtra_pares(x):
    """ função que retorna somente os valores pares de determinada tupla
    tuple -> tuple"""
    par = ()
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    if (x1%2==0):
        par = par + (x1,)
    elif (x2%2==0):
        par = par + (x2,)
    elif (x3%2==0):
        par = par + (x3,)
    elif (x4%2==0):
        par = par + (x4,)
    return par