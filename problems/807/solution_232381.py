def conta_frases(frase):
    '''função que conta o número de frases'''
    while frase:
    reticencias=str.count(frase,'...')
    w=reticencias
    ponto=str.count(frase,'.')
    x=ponto
    exclamacao=str.count(frase,'!')
    y=exclamacao
    interrogacao=str.count(frase,'?')
    z=interrogacao
    total= x+y+z+w
    return total