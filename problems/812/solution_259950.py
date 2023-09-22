from math import *

def retira_pontuacao(texto):
    """Retorna o texto original sem pontuacoes dado um texto com pontuacoes"""
    x = str.replace(texto, ('-'), ' ')
    y = str.replace(x, (','), ' ')
    z = str.replace(y, (':'), ' ')
    w = str.replace(z, (';'), ' ')
    r = str.replace(w, ('.'), ' ')
    s = str.replace(r, ('!'), ' ')
    a = str.replace(s, ('?'), ' ')
    return a

def inverte(texto):
    """Retorna um texto invertido e sem pontuacoes dado um texto"""
    b = str.lower(retira_pontuacao(texto))
    c = str.split(b)[::-1]
    d = str.join(' ',c)
    return d