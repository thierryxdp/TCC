def colchao(medidas,H,L):
    '''dada as medidas do colchão e da porta, retorna 'true'
    caso o colchão passe e 'false' caso não passe;
    list,int,int -> bool'''
    if medidas[0]<H and medidas[1]<L:
        return bool(1==1)
    elif medidas[0]<L and medidas[1]<H:
        return bool(1==1)
    else:
        return bool(2==1)