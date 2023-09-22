def colchao(medidas,H,L):
    """Entrada: lista, int, int
       Retorno: Bool"""
    if H == medidas[1] or L == medidas[0]:
        return False    
    return H > medidas[1] and L > medidas[0]