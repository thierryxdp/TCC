def conta_frases(frase):
    """docstring""" 
    frase= str.replace(texto, '...', '.')
    frase= str.replace(texto, '!', '.')
    frase= str.replace(texto, '?', '.')
    frase= str.split (frase)
    return  len ( frase )