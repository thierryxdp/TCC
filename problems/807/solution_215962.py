def conta_frases(frase):
    """Funcao calcula e retorna a quantidade de frases em um texto;string-->int"""
    a=frase.replace('...','.')
    b=a.replace('...','.')
    c=b.replace('!','.')
    d=c.replace('?','.')
    e=d.split('.')
    return len(e)-1