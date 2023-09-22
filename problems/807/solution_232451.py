def conta_frases(frase):
    '''função que conta o número de frases'''
    ponto=str.count(frase,'.')
    x=ponto-1
    exclamacao=str.count(frase,'!')
    y=exclamacao
    interrogacao=str.count(frase,'?')
    z=interrogacao
    total= (x+y+z)
    return total