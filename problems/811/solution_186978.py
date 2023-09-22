def colchao(medidas,H,L):
    """Funcao que calcula se é possivel passar um colchao por uma porta,
    dados: a (medida) de dimensoes do colchao e a altura (H) e largura (L)
    da porta.
    list, int, int -> bool"""

    B = medidas[1]
    C = medidas[2]

    if B > H and C > H and B > L and C > L:
        return False
    
    else:
        return True