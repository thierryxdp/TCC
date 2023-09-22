def retira_pontuacao(frase):
	"""Função que retorna uma frase onde todos os seus caracteres de pontuação tenham sido substituídos por um espaço
	Entrada: string
	Saída: string"""
	return frase.replace("-", " ").replace(",", "").replace(":", "").replace(";", "").replace(".", "").replace("!", "").replace("?", "")

def inverte(frase):
	"""Função que retorna a mesma frase de entrada, porém com as palavras em ordem inversa, sem letras maiúsculas e sem pontuação
	Entrada: string
	Saída: string"""
	
	return retira_pontuacao(str.lower(" ".join(frase.split()[::-1])))