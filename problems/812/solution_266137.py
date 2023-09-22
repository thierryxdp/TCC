def retira_pontuacao(texto):
  	'''substitui a pontuacao (travessao, virgula, 
    dois pontos, ponto final e ponto e virgula) por 
    espacos em branco
    str -> str'''
  	pontuacoes = ['-',',','.',';',':']
  	list_frase = list(texto)

  	for pontuacao in pontuacoes:
	    for pos,char in enumerate(texto):
    	 	 if char == pontuacao:
        		list_frase[pos] = ' '
  	frase = ''.join(list_frase)
  	return frase