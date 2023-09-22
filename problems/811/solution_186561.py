def colchao(medidas,H,L):
    """Retorna um booleano respondendo se um colchao passa por uma
    porta a partir das medidas do colchao e da porta dadas como entrada.
    list -> bool"""
    if medidas[1]<=H or medidas[2]<=H:
        return True 
    if medidas[1]<=L or medidas[2]<=L:
        return True
    else:
        return False