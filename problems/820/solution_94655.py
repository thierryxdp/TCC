def posLetra(string,letra,numero):
	'''
	->'''
	lista_string = list(string)
	lista_vazia=[]
	contador1=0
	contador2=0
	qnt_letras=len(lista_string)
	while contador1<qnt_letras or contador2==numero:
		if letra==lista_string[contador1]:
			contador2=contador2 + 1
		contador1=contador1+1
	if contador2<numero:
		return -1
	else: 
		return contador1