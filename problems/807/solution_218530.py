def conta_frases(frase):
    """Conta o número de frases de uma string,
    string->int"""
    a=str.count(frase,'!')
    b=str.count(frase,'.')
    c=str.count(frase,'?')
    d=str.count(frase,'...')
    return a+b+c+d