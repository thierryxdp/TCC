def retira_pontuacao(frases):
    '''  '''
    a = str.replace(frases, ('-'), ' ')
    b = str.replace(a, (','), ' ')
    c = str.replace(b, (':'), ' ')
    d = str.replace(c, (';'), ' ')
    e = str.replace(d, ('.'), ' ')
    f = str.replace(e, ('!'), ' ')
    g = str.replace(f, ('?'), ' ')
    return g