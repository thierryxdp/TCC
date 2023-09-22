def conta_frases(texto):
    return len(texto.split('.')) or len(texto.split('?')) and len(texto.split('...')) or len(texto.split('!'))