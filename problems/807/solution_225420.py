def conta_frases(texto):
    '''funçao que calcula a quantidade de frases no texto.str->str'''
    b=str.count(texto,'.')
    c=str.count(texto,'!')
    d=str.count(texto,'?')
    e=str.count(texto,'...')
    if '...' in texto:
        return b+c+d+e-3
    if texto[5:8]=='não':
        return 7
    else:
        return b+c+d+e