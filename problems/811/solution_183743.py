def colchao(medidas,H,L):
	''' Função que determina se o colchão passa ou não pela porta, de acordo com a sua altura, largura e profundidade e a largura e altura da porta
    int->str'''
	lista_colchao=list(medidas)
	if lista_colchao[1]<=H and  lista_colchao[0]<=L:
		return 'True'
	else:
		return 'False'