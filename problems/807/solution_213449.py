def conta_frases(frase):
    """função que recebe um texto de entrada e retorna o número de frases que ele contém;
    str->int"""
    frase= frase.replace('...','.')
    frase= frase.replace('?','.')
    frase= frase.replace('!','.')
    frase= str.count(frase,'.')
    return frase