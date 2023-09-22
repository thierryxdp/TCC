def retira_pontuacao(frase):
    """Funçao que receba uma frase e remove todos os elementos de pontuação contidas nelas deixando apenas 
o espaço entre os lugares, str>str"""
    pontuacao = '-,:;/?!.'
    pontuacao in frase:
		frase=frase.replace(p,' ')
	return frase