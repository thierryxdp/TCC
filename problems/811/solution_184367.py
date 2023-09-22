def colchao(medidas,H,L):
    """
    float, 2 int->bool
	:param medidas: As medidas do colchao
    :param H: A altura da porta da casa
    :param L: A largura da porta da casa
    :return: Retorna uma função booleana dizendo se o colchão passa pela porta
    """
    menorvalor=0
    maiorvalor=0
    if H>=L:
        menorvalor=L
        maiorvalor=H
    else:
        menorvalor=H
        maiorvalor=L
    if medidas[0] <= menorvalor and medidas[1] <= maiorvalor:
        return True
    else:
        return False