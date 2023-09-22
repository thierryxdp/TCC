def retira_pontuacao(texto):
  	'''substitui a pontuacao por espacos em branco
    str -> str'''
  	pontuacoes = ['-',',','.',';',':','?','!']
  	list_frase = list(texto)

  	for pontuacao in pontuacoes:
	   for pos,char in enumerate(texto):
    	 	 if char == pontuacao:
        		list_frase[pos] = ' '
  	frase = ''.join(list_frase)
  	return frase

def inverte(frase):
  	'''inverte a ordem das palavras de uma frase qualquer
    retirando a pontuacao e deixando todas as letras minusculas
    str -> str'''
  	palavras = retira_pontuacao(frase).lower().split()
  	frase_invertida = ' '.join(palavras[::-1])
  	return frase_invertida