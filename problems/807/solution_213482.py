def conta_frases(frase):
    '''recebe uma frase e retorna frases tem nela
    str->int'''
    p=str.count(frase,'.')
    s=str.count(frase,'!')
    r=str.count(frase,'?')
    q=str.count(frase,'...')
    return (p+s+r)-2*q