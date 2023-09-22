def conta_frases(texto):
    """dado um texto a funcao retorna o numero de 
    frases contidas nele; str->int"""
    texto=texto.replace('!','.')
    texto=texto.replace('?','.')
    texto=texto.replace('...','.')
    return texto.count('.')