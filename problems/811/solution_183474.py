def colchao(medidas,H,L):
    '''Dados a medida do colchão medidas, a altura da porta H e o comprimento da porta L, retorne se o colchão passa pela porta;
    lista,int,int -> bool'''
    if medidas[1]<L or medidas[2]<H:
        return True
    else:
        return False