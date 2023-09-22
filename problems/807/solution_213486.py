def conta_frases(frase):
    '''recebe uma string e retorna quantas frases tem nela
    str->int'''
    p=str.count(frase,'.')
    s=str.count(frase,'!')
    r=str.count(frase,'?')
    q=str.count(frase,'...')
    return (p+s+r)-2*q