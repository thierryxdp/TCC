def retira_pontuacao(frase: str) -> str:
    '''
    Retorna frase dada sem caracteres de pontuação, substituindo-os por um espaço
    '''
    frase = frase.replace("-", " ")
	frase = frase.replace(",", " ")
	frase = frase.replace(":", " ")
	frase = frase.replace(";", " ")
	frase = frase.replace(".", " ")
	frase = frase.replace("!", " ")
	frase = frase.replace("?", " ")
	return frase