def conta_frases(frase):
    '''função que conta a quantidade de frases.
    split()'''
    frase = (string.replace(frase, '.', '...', 1)
    ponto = (frase.count('.'))
    exclamacao = (frase.count('!'))
    interrogacao = (frase.count('?'))
    total = exclamacao + interrogacao + ponto
    return total