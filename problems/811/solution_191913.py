def colchao(medidas,H,L):
    """Dada uma lista 'medidas' que possui as dimensões do colchão em ordem 
    crescente, em centímetros; e dois números inteiros 'H' e 'L' que representam
    respectivamente a altura e a largura da porta em centímetros retorna 'True'
    caso o colchão passe pela porta e 'False' caso não.
    list, int, int -> bool"""
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    if A<=H and B<=L:
        return True
    elif A<=H and C<=L:
        return True
    elif B<=H and C<=L:
        return True
    elif C<=H and B<=L:
        return True
    elif A<=L and C<=H:
        return True
    elif A<=L and B<=H:
        return True
    else:
        return False