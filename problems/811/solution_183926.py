def maior(a,b):
    if a > b:
        return a
    return b
def menor(a,b):
    if a < b:
        return a
    return b


def colchao(medidas,H,L):
    """Entrada: lista, int, int
       Retorno: Bool"""
       
    return maior(H,L) >= medidas[1] and menor(H,L) >= medidas[0]