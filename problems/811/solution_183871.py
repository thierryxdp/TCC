def colchao(medidas,H,L):
    """Dadas as medidas de um colchão e a altura e largura de uma porta retorna
       se o colchão passa ou não.
       list(int) int int -> bool"""
    
    if medidas[1] < H:
        return True
    elif medidas[1] == H:
        return True
    else:
        return False