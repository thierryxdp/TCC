def retira_pontuacao(frase):
    'Esta função retira os caracteres de pontuação sendo substituinda por espaço'
	'str--> str'
    travesao = str.replace(frase, '-',' ')
	virgua = str.replace(travesao, ',',' ')
	dois_pontos = str.replace(virgua, ':',' ')
	ponto_virgula = str.replace(dois_pontos, ';',' ')
	ponto_final = str.replace(ponto_virgula, '.',' ')
    esclamacao = str.replace(ponto_final, '!',' ')
    interrogacao = str.replace(esclamacao, '?',' ')
	frase_nova = interrogacao
	return frase_nova