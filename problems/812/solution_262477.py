def retira_pontuacao (frase):
	""" dada uma frase, substitui os caracteres de pontuacao por espaços
		:patametro frase: str
    	:return: str """
	frase = str.replace ( frase, "- . ... ? ! ; : ,", " ")
    return frase