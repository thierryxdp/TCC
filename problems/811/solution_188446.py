def colchao(medidas,H,L):
    '''Função que verifica se é possível ou não de passar o
    colchão pela porta da casa.
    medidas(A,B,C)
    A=espessura do colchao
    B=largura do colchao
    C=comprimento do colchao
    H=altura da porta
    L=largura da porta
    float,float,float ->str'''
    if medidas[1]<=H:
        return True
    elif medidas[1]<=L:
        return True
    elif medidas[2]<=H:
        return True
    elif medidas[2]<=L:
        return True
    else:
        return False