def colchao(medidas,H,L):
    """código que analisa se um colchao de dimensoes medidas
    passa por uma porta de altura H e largura L"""
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    if max(A,B,C) > H:
        return False
    elif max(A,B,C) > L and (A + B + C - max(A,B,C) - min(A,B,C) > L):
        return False
    else:
        True