def conta_frases(frase):
    """Conta o número de frases de uma string,
    string->int"""
    x=len(frase)
    a=str.count(frase,'!')
    b=str.count(frase,'. ',0,x-4)
    c=str.count(frase,'?')
    d=str.count(frase,'...')
    e=str.count(frase,'.',x-1)
    return a+b+c+d+e