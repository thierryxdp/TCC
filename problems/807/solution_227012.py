def conta_frases(frase):
    '''função que conta a quantidade de frases.
    split()'''
    frase1 = (str.replace(frase,'...','.')
    ponto = (frase1.count('.'))
    exclamacao = (frase1.count('!'))
    interrogacao = (frase1.count('?'))
    total = exclamacao + interrogacao + ponto
    return total