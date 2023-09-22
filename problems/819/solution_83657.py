def filtraMultiplos (x,n):
    
    '''
    
    '''
    listaMul=[]
    proximo=0
    while proximo<len(x):
        if x[proximo]%n==0:
            listaMul= listaMul+list(x[proximo])
        proximo=proximo+1
    return listaMul