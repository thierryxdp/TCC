def filtra_pares(a,b,c,d):
	'''Faz a filtragem da tupla(a,b,c,d) e retorna uma nova tupla
	contendo apenas os elementos pares'''
    '''int,int,int,int->tuple'''
    a1=a%2
    b1=b%2
    c1=c%2
    d1=d%2
    if a1==0:
        if b1==0:
            if c1==0:
                if d1==0:
                    return (a,b,c,d)