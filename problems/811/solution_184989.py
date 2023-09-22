def colchao(medidas, H, L):
    """Funcao que compara as medidas de um colchao e diz se o colchao passa ou nao pela porta;
    list, int, int -> bool"""
    
    a, b = medidas[0:2]
    
    if L > a and H > b:
        return True
    elif L > b and H > a:
        return True
    else:
        return False