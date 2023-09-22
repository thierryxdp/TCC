def conta_frases(texto):
    '''Função que calcula quantas frases tem no texto
    sendo cada frase determinada pelo ponto de interrogação
    exclamação final e as reticÊncias
    entrada=string
    saida=int'''
    h=texto.replace(' ','')
    d = str.replace(h,('...'),' ')
    r = str.replace(d, ('.'), ' ')
    s = str.replace(r, ('!'), ' ')
    a = str.replace(s, ('?'), ' ')
    g=a.split(' ')
    return len(g)-1