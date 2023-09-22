def conta_frases(s):
    """conta a quantidade de frases em um texto de entrada"""
    return len(str.split(s,'!','.'))