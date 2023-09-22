def retira_pontuacao(frase):
    'Esta função retira os caracteres de pontuação sendo substituinda por espaço'
	'str--> str'
    travesao = str.replace(frase, '-',' ')
	virgua = str.replace(travesao, ',',' ')
	dois_pontos = str.replace(virgua, ':',' ')
	ponto_virgula = str.replace(dois_pontos, ';',' ')
	ponto_final = str.replace(ponto_virgula, '.',' ')
	frase_nova = ponto_final
	return frase_nova