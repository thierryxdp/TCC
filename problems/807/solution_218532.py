def conta_frases(frase):
    """Conta o número de frases de uma string,
    string->int"""
    x=len(frase)-1
    a=str.count(frase,'!')
    b=str.count(frase,'. ')
    c=str.count(frase,'?')
    d=str.count(frase,'...')
    e=str.count(frase,'.',x)
    return a+b+c+d