def conta_frases(frases):
    """Recebe uma string e retorna a quantidade de frases na string"""
    frases.strip
    frases.replace('!', '.', 1)
    frases.replace('?', '.', 1)
    frases.replace('...', '.', 1)
    return len(frases.split('.'))