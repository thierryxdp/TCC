def filtra_pares(a,b,c,d):
    '''Dados os quadro elementos inteiros da tupla, retorna apenas os elementos pares
    tuple->tuple'''
    A=a%2
    B=b%2
    C=c%2
    D=d%2
    if A==0 and B==0 and C==0 and D==0:
        return (a,b,c,d)
    elif A!=0 and B!=0 and C!=0 and D!=0:
        return ()
    elif A!=0 and B==0 and C==0 and D==0:
        return (b,c,d)
    elif A!=0 and B!=0 and C==0 and D==0:
        return (c,d)
    elif A!=0 and B!=0 and C!=0 and D==0:
        return (d)