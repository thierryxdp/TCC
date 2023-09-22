def conta_frases(frase):
    '''função que conta o número de frases'''
    ponto=str.count(frase,'.')
    x=ponto
    exclamacao=str.count(frase,'!')
    y=exclamacao
    interrogacao=str.count(frase,'?')
    z=interrogacao
    reticencias=str.count(frase, '...')
    w=reticencias
    x+y+z+w=total
    return total