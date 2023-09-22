def filtra_pares(a): #Start your python function here
    for x in a:
        if a.count(x) > 1:
            return x
        else:
            return ()