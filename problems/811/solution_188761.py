def colchao(medidas,H,L):
    '''dada as medidas do colchão e da porta, retorna 'true'
    caso o colchão passe e 'false' caso não passe;
    list,int,int -> bool'''
    if medidas[0]<medidas[1] and medidas[1]<medidas[2]:
        return true
    elif medidas[0]<medidas[2] and medidas[1]<medidas[1]:
        return true
    else:
        return false