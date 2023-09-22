def colchao(medidas, h, l):
    """dadas as medidas do colchao, altura e largura da porta, retorna verdadeiro se o colchao passa e falso se nao passa pela porta
    list, int, int -> bool"""
    if medidas[0]<= h and medidas[1] <= l or medidas[1] <= h and medidas[0] <=l:
        return True
    else:
        return False