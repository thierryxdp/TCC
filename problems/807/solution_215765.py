def conta_frases(frase):
    """Funcao calcula e retorna a quantidade de frases em um texto;srting-->int"""
    frase=('.' and '!' and '?' and '...")
    if '.':
           return 1       
    return len(frase)