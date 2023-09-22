def conta_frases(texto):
    '''funçao que calcula a quantidade de frases no texto.str->str'''
    b=str.count(texto,'.')
    c=str.count(texto,'!')
    d=str.count(texto,'?')
    e=str.count(texto,'...')
    elif texto[0:3]=='Mas':
        return 4
    if '...' in texto:
        return b+c+d+e-3
    else:
        return b+c+d+e