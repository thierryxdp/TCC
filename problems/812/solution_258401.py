def retira_pontuacao(frase):
	"""Função que retorna uma frase onde todos os seus caracteres de pontuação tenham sido substituídos por um espaço
	Entrada: string
	Saída: string"""
	return frase.replace("-", " ").replace(",", " ").replace(":", " ").replace(";", " ").replace(".", " ").replace("!", " ").replace("?", " ")