def conta_frases(frase):
    """Conta o número de frases de uma string,
    string->int"""
    x=len(frase)
    a=str.count(frase,'!')
    b=str.count(frase,'.')
    c=str.count(frase,'?')
    d=str.count(frase,'...')
    if d>0 and b>0:
        return a+b+c+d-3
    else:
        return a+b+c+d