def retira_pontuacao(texto):
    '''função que retorna uma frase sem pontuação,
    substituindo por espaço'''

    x = str.replace(texto, ('-'), ' ')
    y = str.replace(x, (','), ' ')
    z = str.replace(y, (':'), ' ')
    w = str.replace(z, (';'), ' ')
    r = str.replace(w, ('.'), ' ')
    s = str.replace(r, ('!'), ' ')
    a = str.replace(s, ('?'), ' ')
    return a
def inverte (texto):
    '''função que retorna o inverso de uma frase dada, contendo
    as mesmas palavras da frase de entrada na ordem inversa'''
    b = str.lower(retira_pontuacao(texto))
    c = str.split(b)[::-1]
    d = str.join(' ',c)
    return d