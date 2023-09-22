def conta_frases(frase):
    """Retorna o número de frases a partir de um texto""" 
    frase= str.replace(frase, '...', '.')
    frase= str.replace(frase, '!', '.')
    frase= str.replace(frase, '?', '.')
    frase= str.split (frase,'.')
    return  len ( frase )-1