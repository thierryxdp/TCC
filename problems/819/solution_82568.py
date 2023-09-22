def filtraMultiplos(l,n):
    ''
    proximo=0
    m=[]
    while proximo <len(l):
        if proximo%n == 0:
            m=m + (proximo,)
        proximo=proximo + 1 
    return m