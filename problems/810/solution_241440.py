def inverte(frase):
    """Recebe uma frase e retorna o contrario da composição das frases.
    str -> str"""
    frase = frase.replace(',', ' ')
    frase = frase.replace('-', ' ')
	frase = frase.replace('.', ' ')
    frase = frase.replace('!', ' ')
    frase = frase.replace('?', ' ')
    frase = frase.lower()
    
    separado = reversed(frase.split())
    return ' '.join(separado)