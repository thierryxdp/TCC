def conta_frases(frase):
    '''função que conta o número de frases'''
    ponto=str.split(frase,'.')
    x=len(ponto)
    exclamação=str.split(frase,'!')
    y=len(exclamação)
    interrogação=str.split(frase,'?')
    z=len(interrogação)
    total= x+y+z
    return total