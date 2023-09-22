def conta_frases(frase):
    '''função que conta a quantidade de frases.
    split()'''
    
    ponto = (frase.split('.'))
    interrogacao = (frase.split('?'))
    tres_ponto = (frase.split('...'))
    total = len(ponto) + len(interrogacao)+len(tres_ponto)
    return total