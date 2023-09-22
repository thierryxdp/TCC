from math import *

def retira_pontuacao(frase):
    '''
    Dada uma frase, retira a pontuacao da frase e substitui por espaço.

    Uso:
    retira_pontuacao(frase)

    Entrada:
    - frase (str, obrigatório): variavél 1

    Saída:
    - A frase original sem nenhum sinal de pontuação. (str)
    '''

    x = str.replace(frase, ('-'), ' ')
    y = str.replace(x, (','), ' ')
    z = str.replace(y, (':'), ' ')
    w = str.replace(z, (';'), ' ')
    r = str.replace(w, ('.'), ' ')
    s = str.replace(r, ('!'), ' ')
    a = str.replace(s, ('?'), ' ')
    return a