def conta_frases(frase):
    '''função que conta o número de frases'''
    w=0
    ponto=str.count(frase,'.')
    x=ponto
    exclamacao=str.count(frase,'!')
    y=exclamacao
    interrogacao=str.count(frase,'?')
    z=interrogacao
    if '...' in frase:
        w+=1
    total= (x+y+z+w)
    return total