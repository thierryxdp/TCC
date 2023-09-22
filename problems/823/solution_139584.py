def faltante(qb):
    n = len(qb) + 1
    s = n
    qb.sort()
    
    for i in range(1,n):
        if(qb[i-1] !=1):
            s = i
            break
    return s