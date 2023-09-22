def conta_frases(texto):
    ''' dada um texto com frases terminadas em '!",".","?" ou "...", a funao retorna a quantidade de frases desse texto
        str -> int'''
    return (texto.count('.')  + texto.count('!') + texto.count('?')) - 2*texto.count('...')