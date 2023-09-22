from math import *

def retira_pontuacao(frase):
    '''Função que retira todas as pontuações da variavel
    frase. entrada=(string, frase com putuação) 
    saida=(string, frase sem putuação)'''

    x = str.replace(frase, ('-'), ' ')
    y = str.replace(x, (','), ' ')
    z = str.replace(y, (':'), ' ')
    w = str.replace(z, (';'), ' ')
    r = str.replace(w, ('.'), ' ')
    s = str.replace(r, ('!'), ' ')
    a = str.replace(s, ('?'), ' ')
    return a