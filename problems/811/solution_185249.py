def colchao(medidas,H,L):
    """Funcao que resolve esse problema, onde mediddas é uma lista com os tamanhos inteiros A, B e C, e H e L são os tamanhos inteiros da altura e largura da porta, respectivamente.
    list, int, int -> bool"""
    A,B,C=medidas
    if B < H or C < L:
        return True
    else:
        return False