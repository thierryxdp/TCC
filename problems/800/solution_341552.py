def total(listaCompras, precosCompras):
	'''Uma função que dependendo da sua lista de compras, retorna o valor dos produtos'''
    '''list, dic -> dic'''
    precosFinal = {}
    for valor in listaCompras:
        if valor in precosCompras:
            precosFinal[valor] = precosCompra[valor]
	return precosCompras