def colchao(medidas,H,L):
    '''Retorna se João consegue passar o colchão pela porta
    dadas a altura (H) e largura (L) da porta e as medidas do colchão;
    lista,int,int->'''
    
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    
    if H>= A and L>=B:
        return True
    if H>=B and L>=A:
        return True
    else:
        return False