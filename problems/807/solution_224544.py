def conta_frases(texto):
    return len(texto.split('.', maxsplit=1)) and len(texto.split('?', maxsplit=1)) and len(texto.split('...', maxsplit=1)) and len(texto.split('!', maxsplit=1))