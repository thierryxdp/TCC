def inverte(frase: str) -> str:
    '''
    Retorna frase invertida e sem pontuação dada uma frase
    '''
	frase = frase.replace("-", "")
	frase = frase.replace(",", "")
	frase = frase.replace(":", "")
	frase = frase.replace(";", "")
	frase = frase.replace(".", "")
	frase = frase.replace("!", "")
	frase = frase.replace("?", "")
    return frase.reverse