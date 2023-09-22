def conta_frases(frase):
    '''função que conta o número de frases'''
    ponto=str.count(frase,'.')
    x=ponto
    exclamacao=str.count(frase,'!')
    y=exclamacao
    interrogacao=str.count(frase,'?')
    z=interrogacao
    reticencias=str.strip(frase, '...')
    w=reticencias
    k=len(w)
    total= (x+y+z)+k
    return total