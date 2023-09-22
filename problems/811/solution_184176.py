def colchao(medidas,H,L):
    """Dada as medidas em centimetros de um colchao e os numeros inteiros "H" e "L" referentes a medida de uma porta, a funcao retorna True caso o colchao consiga passar pela porta"""
    """entrada: lista, int, int
    saida: boolean"""
    
    if medidas [1] <= H:
        return True
    elif medidas [1] <= L:
        return True
    elif medidas [2] <= H:
        return True
    elif medidas [2] <= L:
        return True
    else:
        return False