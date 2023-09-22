def conta_frases(texto):
    '''função recebe um texto e retorna o número de frases que o texto possui.
    string -> int'''
    if '...' in texto:
        return texto.count('!') + texto.count('?') + texto.count('.') - texto.count('...')*2
    else:
        return texto.count('!') + texto.count('?') + texto.count('.')