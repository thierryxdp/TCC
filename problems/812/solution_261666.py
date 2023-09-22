def retira_pontuacao(frase):
	"""Função que retira toda a pontuação da frase
    str -> str"""
    frase=str.replace(frase, '_', ' ')
    frase=str.replace(frase, ',', ' ')
    frase=str.replace(frase, ':', ' ')
    frase=str.replace(frase, ';', ' ')
    frase=str.replace(frase, '.', ' ')
	return frase