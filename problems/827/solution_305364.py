def filtraMultiplos(t,n):
    '''''''
    pares=[]
    proximo=0
    for proximo in len(t):
        
        if t[proximo]%n==0:
            pares=pares +[t[proximo]]
        proximo=proximo+1
    return pares