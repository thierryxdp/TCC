def colchao(medidas,H,L):
    """Recebe as medidas do colchao e altura e largura das portas da casa de João e retorna se é possível o colchão atravessá-las
    :param medidas: list
    :param H: int
    :param L: int
    :return: bool
    """
    if medidas[1:2]>H:
        return False
    else:
        return True