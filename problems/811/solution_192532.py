def colchao(medidas,H,J):
    '''função que retorna se um colchão passa pela porta dada as medidas inteiras do colchão
    e as medidas da altura(H) e largura(L) da porta;
    list[int,int,int],int,int->bool'''
    if (medidas[0]<=L and medidas[1]<=H) or (medidas[0]<=H and medidas[1]<=L):
        return True
    else:
        return False