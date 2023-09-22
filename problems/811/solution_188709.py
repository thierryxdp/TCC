def colchao(medidas,H,L):
    """retorna se um colchao de medidas[A,B,C] de entrada
    passa atraves de uma porta de altura H  e largura L
    de entrada.
    list,int,int-->bool"""
    if medidas[1] and medidas[2] > H and L:
        return False
    else:
        True