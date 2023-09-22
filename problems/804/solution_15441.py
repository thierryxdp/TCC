def filtra_pares(tup):
    if tup%2==0:
        par=list(filter(filtra_pares,[tup]))
        return par
    else:
        return False
    

    #Start your python function here