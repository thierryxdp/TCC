def conta_frases(frase):
    '''função que conta a quantidade de frases.
    split()'''
    
    ponto = (frase.count('.'))
    exclamacao = (frase.count('!'))
    interrogacao = (frase.count('?'))
    tres_ponto = (frase.count('...'))
    total = len(ponto) + len(exclamacao) + len(interrogacao)+len(tres_ponto)
    return total