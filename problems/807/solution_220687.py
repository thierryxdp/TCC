def conta_frases(frases.strip):
    """Recebe uma string e retorna a quantidade de frases na string"""
    frases.replace('!', '.', 1)
    frases.replace('?', '.', 1)
    frases.replace('...', '.', 1)
    return len(frases.split('.'))