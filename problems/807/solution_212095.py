def conta_frase(texto):
    '''Função que, dado um texto, conta o número de frases que aparecem
    neste texto. Vale ressaltar que cada frase do texto é terminada com
    um ponto final, um ponto de exclamação, um ponto de interrogação ou
    reticências
    str -> int
    '''
    if str.count(texto,'...') > 0:
        texto = str.replace(texto,'...','&')
        a = str.count(texto,'&')
        b = str.count(texto,'!')
        c = str.count(texto,'?')
        d = str.count(texto,'.')
    else:
        a=0
        b = str.count(texto,'!')
        c = str.count(texto,'?')
        d = str.count(texto,'.')
    return a+b+c+d