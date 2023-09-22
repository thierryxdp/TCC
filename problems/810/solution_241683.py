def invert(frase):
    listaPalavras=retira_pontuacao(frase).split()
    return listaPalavras[::(-1)]

def retira_pontuacao(frases):
    '''retira as seguintes pontuaçoes de uma string (./?/!/
    ,/-/:/;) e subrtitui por um espaço'''
    a = str.replace(frases, ('-'), ' ')
    b = str.replace(a, (','), ' ')
    c = str.replace(b, (':'), ' ')
    d = str.replace(c, (';'), ' ')
    e = str.replace(d, ('.'), ' ')
    f = str.replace(e, ('!'), ' ')
    g = str.replace(f, ('?'), ' ')
    return g