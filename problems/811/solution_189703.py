def colchao(medidas,H,L):
    """medidas:altura, largura e comprimento do colchão em cm
    H e L: altura e a largura das portas em cm 
    Retorna True se o colchão passa pelas portas e False caso contrário"""
    if medidas[1]<=H and medidas[0]<=L:
        return True
    else:
        return False