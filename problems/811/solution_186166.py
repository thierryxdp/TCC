def colchao(medidas,H,L):
    """A função recebe as medidas do colchão e da porta,
	e verifica se o colchão passa pelo local;
	lista|int|int --> bool"""
	
    tamanho = medidas[1]
    if tamanho < H and L:
        return False
    else:
        return True