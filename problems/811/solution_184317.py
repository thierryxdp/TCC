def colchao(medidas,H,L):
    """
    float, 2 int->bool
	:param medidas: As medidas do colchao
    :param H: A altura da porta da casa
    :param L: A largura da porta da casa
    :return: Retorna uma função booleana dizendo se o colchão passa pela porta
    """
    entrada = input("A B C").split()
    A, B, C = int(entrada[0], int(entrada[1], int(entrada[2])
    if A >= 1 and A <= 25 and B >= 1 and B <= 200 and C >= 1 and C <= 220
		return True
    else:
    	return False
    entrada = input("Porta").split()
    H,L = int(entrada[0], int(entrada[1])
    if H >= 1 and H <= 200 and L>=1 and L <= 100:
    	return True
    else:
        return False
    if (A and B) > (H and L) or (A and C) > (H and L) or (B and C) > (H and L):
    	return True
    else:
        return False