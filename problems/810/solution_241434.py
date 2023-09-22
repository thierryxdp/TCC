def inverte(frase):
    """Recebe uma frase e retorna o contrario da composição das frases.
    str -> str"""
    frase = frase.replace(',', ' ')
    frase = frase.replace('-', ' ')
	frase = frase.replace('.', ' ')
    
    separado = reversed(frase.split()).lower
    return ' '.join(separado)