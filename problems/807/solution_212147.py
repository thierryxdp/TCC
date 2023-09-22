def conta_frases(texto):
    """Retorna o numero de frases em um texto ; str--> int"""
    return texto.count('.') + texto.count('!') + texto.count('?') - 2*texto.count('...')