def conta_frases(frase):
    """docstring""" 
    frase= str.replace(frase, '...', '.')
    frase= str.replace(frase, '!', '.')
    frase= str.replace(frase, '?', '.')
    frase= str.split (frase,'.')
    return  len ( frase )-1