def conta_frases(frase):
    '''Função que conta o numero de palavras de uma frase'''
    return str.count(frase,'. ') + str.count(frase,'...') + str.count(frase,'!') + str.count(frase,'?')