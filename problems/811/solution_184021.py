def colchao(medidas,H,L):
    """função que retorna True, se o colchão passa pelas portas, e False, caso contrário, a partir das dimensões do colchão em centímetros, da menor pra maior, e da altura H e largura L das portas
    list, int, int -> bool"""
    return medidas[1] <= H or medidas[1] <= L