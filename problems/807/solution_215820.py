def conta_frases(frase):
    """Funcao calcula e retorna a quantidade de frases em um texto;string-->int"""
    frase=('.' and '!' and '?' and '...')
    if '.' not in '...':
           return True       
    return str.count(frase)