def conta_frase(texto):
    '''função recebe um texto e retorna o número de frases que o texto possui.
    string -> int'''
    return texto.count('!') + texto.count('?') + texto.count('.')