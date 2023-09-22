def qtd_divisores(x):
    m=[]
    for e in range(x):
        if x%e+1==0:
            m+=e
        else:
            None
    
    
    return len(m)