def colchao(medidas,H,L):
    '''dada as medidas do colchão e da porta, retorna 'true'
    caso o colchão passe e 'false' caso não passe;
    list,int,int -> bool'''
    if medidas[0]<h and medidas[1]<l:
        return bool(1==1)
    elif medidas[0]<l and medidas[1]<h:
        return bool(1==1)
    else:
        return bool(2==1)