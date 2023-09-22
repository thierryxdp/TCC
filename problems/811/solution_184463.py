def colchao(dimensoes,H,L):
    """dimensões:altura, largura e comprimento do colchão em cm
    H e L: altura e a largura das portas em cm 
    Retorna True se o colchão passa pelas portas e False caso contrário"""
    if dimensoes[1]<=H and dimensoes[0]<=L:
        return True
    else:
        return False