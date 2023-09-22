def conta_frases(frase):
    '''função que conta a quantidade de frases.
    split()'''
    
    ponto = (frase.count('.'))
    exclamacao = (frase.count('!'))
    interrogacao = (frase.count('?'))
    total = ponto + exclamacao + interrogacao
    return total