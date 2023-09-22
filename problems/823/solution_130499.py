def faltante(lista):
	'''
	->'''
	contador1=0
	saida = 'certo'
	while saida < len(lista):
		if lista[contador1]!= (contador1 +1):
			saida = contador1 +1
		else:
			saida = 'certo'
		contador1 = contador1+1
	if saida == 'certo':
        return len(lista) +1
	else:
		return saida