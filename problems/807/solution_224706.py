def conta_frase (frase):
    """ dado um texto, conta as frases presentes no texto
    	:parametro frase: str
        return: int"""
    frase = str.replace(frase, '...', '#')
    frase = str.replace(frase, '.', '#')
    frase = str.replace(frase, '!', '#')
    frase = str.replace(frase, '?', '#')
    	return len(str.split(frase,'#'))=1