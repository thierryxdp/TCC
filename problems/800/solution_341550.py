def total(listaCompras, precosCompra):
	'''Uma função que dependendo da sua lista de compras, retorna o valor dos produtos'''
    '''list, dic -> dic'''
	listaComprasMod = listaCompras.split()
    precosFinal = {}
    for valor in listaComprasMod:
        if valor in precosCompras:
            precosFinal[valor] = precosCompra[valor]
	return precosCompras