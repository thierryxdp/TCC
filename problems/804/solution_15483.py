def filtra_pares(tup):
    L=list(tup)
    for L in tup:
        if L%2==0:
            return True
        else:
            return False
    
 par=list(filter(filtra_pares,L))
    #Start your python function here