def faltante(lista):
	'''
	->'''
	contador1=0
    saida = 'certo'
	while saida == 'certo':
        if lista[contador1]!= contador1 +1:
            saida = 'errado'
		else:
            saida = 'certo'
        contador1 = contador1+1
	return contador