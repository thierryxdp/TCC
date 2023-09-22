def conta_frases(frases):
    """Recebe uma string e retorna a quantidade de frases na string"""
    frases.replace('!', '.')
    frases.replace('?', '.')
    frases.replace('...', '.')
    return len(frases.split('.'))