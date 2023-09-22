def conta_frases(frase):
    """Funcao calcula e retorna a quantidade de frases em um texto;string-->int"""
    frase=('. ' and '!' and '?' or '...')
    if '.' not in '...':
           return True
    if '.' not in '..':
        return True
    return len(frase)