def inverte(texto):
    '''Dado um texto inverte a ordem das palavras o texto devidamente invertido e sem nenhum sinal de pontuação; string -> string'''
    from math import *

def retira_pontuacao(texto):
    '''dado um texto retira sua pontuacao; string -> string'''
    x = str.replace(texto, ('-'), ' ')
    y = str.replace(x, (','), ' ')
    z = str.replace(y, (':'), ' ')
    w = str.replace(z, (';'), ' ')
    r = str.replace(w, ('.'), ' ')
    s = str.replace(r, ('!'), ' ')
    a = str.replace(s, ('?'), ' ')
    return a
    b = str.lower(retira_pontuacao(texto))
    c = str.split(b)[::-1]
    d = str.join(' ',c)
    return d