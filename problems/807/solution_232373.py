def conta_frases(frase):
    '''função que conta o número de frases'''
    ponto=str.count(frase,'.')
    x=len(str(ponto))
    exclamacao=str.count(frase,'!')
    y=len(exclamacao)
    interrogacao=str.count(frase,'?')
    z=len(interrogacao)
    reticencias=str.count(frase,'...')
    w=len(reticencias)
    total= x+y+z+w
    return total