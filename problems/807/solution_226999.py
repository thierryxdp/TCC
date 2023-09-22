def conta_frases(frase):
    '''função que conta a quantidade de frases.
    split()'''
    frase = (str.replace(frase,'...','.')
    tresponto = (frase.count('...'))
    ponto = (frase.count('.'))
    exclamacao = (frase.count('!'))
    interrogacao = (frase.count('?'))
    total = exclamacao + interrogacao + tresponto + ponto
    return total