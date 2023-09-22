def conta_frases(frase):
    '''função que conta a quantidade de frases.
    split()'''
    frase = (frase.replace('...','.')
    ponto = (frase.count('.'))
    tres = (frase.count('...'))
    exclamacao = (frase.count('!'))
    interrogacao = (frase.count('?'))
    total = exclamacao + interrogacao + ponto + tres
    return total