def colchao(medidas,H,L):
    """Funcao que diz se o colchao passa na porta dados as medidas do colchao e da porta;
    Entrada: list, int, int
    Saida: bool"""


    if medidas[1]<=H or medidas[2]<=L or medidas[2]<=H or medidas[1]<=L:
        return True
    else:
        return False