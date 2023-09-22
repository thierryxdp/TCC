def conta_frases(frase):
    '''Esta e a funcao que conta o numero de frases que
    aparecem em um texto de entrada
    str -> int'''
    p1=frase.count('.')
    p2=frase.count('!')
    p3=frase.count('?')
    p4=frase.count('...')
    if p4!=0:
        return p1-(3*p4)+p2+p3+p4
    return p1+p2+p3