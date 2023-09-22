def total(listaCompras, precosCompras):
	'''Uma função que dependendo da sua lista de compras, retorna o valor dos produtos'''
    '''list, dic -> dic'''
    for valor in listaCompras:
        if valor in precosCompras:
            precoFinal = precosCompras[valor] + precoFinal
	return precoFinal