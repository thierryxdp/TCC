def conta_frases(frases):
    """Recebe uma string e retorna quantas frases tem nela."""
    frases = frases.replace('?', '.')
    frases = frases.replace('!', '.')
    frases = frases.replace('...', '.')
    
    return len(int(frases.split('.')) - 1)