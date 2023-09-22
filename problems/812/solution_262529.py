def retira_pontuacao(frase):
    """Funçao que receba uma frase e remove todos os elementos de pontuação contidas nelas deixando apenas 
o espaço entre os lugares, str>str"""
    pontuacao = '-,:;/?!'
    for p in pontuacao:
		frase=frase.replace(p,' ')
	return frase