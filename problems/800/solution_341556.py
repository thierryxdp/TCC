def total(listaCompras, precosCompras):
	'''Uma função que dependendo da sua lista de compras, retorna o valor dos produtos'''
    '''list, dic -> dic'''
    precoFinal = 0
    for valor in listaCompras:
        if valor in precosCompras:
            precoFinal = precosCompras[valor] + precoFinal
	return round(precoFinal, 2)