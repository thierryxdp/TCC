def conta_frases(x):
    '''função que conta o número de frases que aparecem no texto, segundo as
    pontuações ali presentes'''
    a=str.strip(x)
    n=str.count(a,' ')
    return n+1