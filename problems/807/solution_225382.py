def conta_frases(texto):
    '''funçao que calcula a quantidade de frases no texto.str->str'''
    a=str.count(texto,',')
    b=str.count(texto,'.')
    c=str.count(texto,'!')
    d=str.count(texto,'?')
    e=str.count(texto,'...')
    if '...' in texto:
        return a+b+c+d+e-3
    else:
        return a+b+c+d+e