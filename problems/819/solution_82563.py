def filtraMultiplos(l,n):
    ''
    proximo=l[0]
    m=[]
    while proximo <len(l):
        if l[proximo]%n == 0:
            m=proximo + 1 
    return m