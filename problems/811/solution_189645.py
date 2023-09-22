def colchao(medidas,H,L):
    """Função que calcula se o colchão consegue passar através das portas da casa do João"""
    if H< medidas[1] and L< medidas[2]:
        return False
    else:
        return True