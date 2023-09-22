def conta_frases(x):
    '''Retorna o npumero de frases que aparecem no texto.
    str -> int'''
    x=str.split(x)
    i=0
    a=0
    while i<len(x):
        if '!' in x[i]:
            a=a+1
            i=i+1
        elif '.' in x[i]:
            a=a+1
            i=i+1
        elif '...' in x[i]:
            a=a+1
            i=i+1
        elif '?' in x[i]:
            a=a+1
            i=i+1
        else:
            i=i+1
    return a