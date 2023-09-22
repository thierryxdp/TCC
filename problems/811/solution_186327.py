def colchao(x,h,l):
    '''
    	Dadas 3 entradas: uma lista de 3 elementos,H e L calcula se
        com as medidas do colchão(lista) é possivel atravessar
        a porta de medidas H e L.
        list,int,int -> bool
    '''
    a=x[0]
    b=x[1]
    c=x[2]
    if (b <= h) or (b <= l):
        return True
    elif (c <= h) or (c <=l):
        return True
    else:
        return False