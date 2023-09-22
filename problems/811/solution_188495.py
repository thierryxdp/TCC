def colchao(medidas,H,L):
    ''' dado as dimensões do colchão e da porta retorna se é possivel que este passe pela porta
    Dc: dimensões do colchão
    Dp: dimensões do colchão'''
    if medidas[1]>H and medidas[2]>H:
        return False
    else:
        return True