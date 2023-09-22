def colchao(medidas,H,L):
    """Calcula se e possivel atravessar o colchao de medidas (A),(B) e (C), por uma porta de altura (H) e largura(L), retornando True se o colchao passa pela porta ou False caso contrario.
    A funcao tem como parametros de entrada as medidas do colchao, organizadas da menor para maior, a altura da porta e sua largura, respectivamente.
    list, int, int -> bool"""
    [A,B,C]=medidas
    if medidas[0]<=L and medidas[2]<=H:
        return True
    elif medidas[2]<=L and medidas[0]<=H:
        return True
    elif medidas[1]<=L and medidas[0]<=H:
        return True
    elif medidas[0]<=L and medidas[1]<=H:
        return True
    elif medidas[1]<=L and medidas[2]<=H:
        return True
    elif medidas[2]<=L and medidas[1]<=H:
        return True
    else:
        return False