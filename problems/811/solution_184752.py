def colchao(medidas, H, L):
    """Função que dadas as medidas de um colchão e a altura(H) e a largura(L) de uma porta retorna se o colchão passa ou não pela porta. lista, int, int --> bool """
    if (medidas[0] <= L) and (medidas[1]  <= H):
        return True
    else:
        return False