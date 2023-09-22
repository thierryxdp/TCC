def conta_frases(frase):
    """Funcao calcula e retorna a quantidade de frases em um texto;srting-->int"""
    frase=('.' and '!' or '?' or '...')
    return len(frase)