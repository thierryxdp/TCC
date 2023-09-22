def retira_pontuacao(frase):
	'''dada uma frase, retona ela sem os caracteres de pontuacao
    str -> str'''
	lista_final = []
	frase_final = ''
	for i in frase:
		lista_final.append(i)
	for i in lista_final:
		if i in '.,:;-!?':
			lista_final[lista_final.index(i)] = ' '
	for i in lista_final:
		frase_final += i
	return frase_final