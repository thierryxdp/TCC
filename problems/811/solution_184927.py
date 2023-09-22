def colchao(medidas, H, L):
    """Funcao que compara as medidas de um colchao e diz se o colchao passa ou nao pela porta;
    list, int, int -> bool"""
    
    a, b = medidas[0:2]
    
    if a < L and b < H:
        return True
    
    else:
        return False