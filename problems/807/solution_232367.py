def conta_frases(frase):
    '''função que conta o número de frases'''
    ponto=str.split(frase,'.')
    x=len(ponto)
    exclamacao=str.split(frase,'!')
    y=len(exclamacao)
    interrogacao=str.split(frase,'?')
    z=len(interrogacao)
    reticencias=str.split(frase,'...')
    total= x+y+z
    return total