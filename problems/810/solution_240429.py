from math import *

def retira_pontuacao(texto):
    '''
    Dada um texto retira a pontuacao da mesmo e substitui por espaço.

    Uso:
    retira_pontuacao(texto)

    Entrada:
    - texto (str, obrigatório): variavél 1

    Saída:
    - O texto original sem nenhum sinal de pontuação. (str)
    '''

    x = str.replace(texto, ('-'), ' ')
    y = str.replace(x, (','), ' ')
    z = str.replace(y, (':'), ' ')
    w = str.replace(z, (';'), ' ')
    r = str.replace(w, ('.'), ' ')
    s = str.replace(r, ('!'), ' ')
    a = str.replace(s, ('?'), ' ')
    return a

def inverte(texto):
    '''
    Dado um texto inverte a ordem das palavras

    Uso:
    inverte(texto)

    Entrada:
    - texto (str, obrigatório): variavél 1

    Saída:
    - O texto devidamente invertido e sem nenhum sinal de pontuação. (str)
    '''
    b = str.lower(retira_pontuacao(texto))
    c = str.split(b)[::-1]
    d = str.join(' ',c)
    return d