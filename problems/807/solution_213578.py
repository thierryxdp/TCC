def conta_frases(frase):
    '''Dado uma string frase, retorne o número de frases; string -> int'''
    a=str.count(frase,'.')
    b=str.count(frase,'!')
    c=str.count(frase,'?')
    d=str.count(frase,'...')
    return a+b+c+d-(3*d)