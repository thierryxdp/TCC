from math import *

def retira_pontuacao(texto):
    ''' funçao que, fornecida um texto pelo usuario, retorna o mesmo,
    porem sem nenhuma pontuação, substituindo por espaços
    str -> str'''

    x = str.replace(texto, ('-'), ' ')
    y = str.replace(x, (','), ' ')
    z = str.replace(y, (':'), ' ')
    w = str.replace(z, (';'), ' ')
    r = str.replace(w, ('.'), ' ')
    s = str.replace(r, ('!'), ' ')
    a = str.replace(s, ('?'), ' ')
    return a