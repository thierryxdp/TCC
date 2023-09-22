def filtra_pares(tup):
    if tup%2==0:
       
        return True
    else:
        return False
    
 par=list(filter(filtra_pares,tup[::1]))
    #Start your python function here