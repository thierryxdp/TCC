def conta_frases (texto):
    frase=texto.split('!', '...', '?', '.')
    return len(frase)