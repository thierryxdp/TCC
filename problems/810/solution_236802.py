def retira_pontuacao(frase):
    '''Função que dada uma frase , retira a pontuação da frase e substitui por espaço'''
    x = str.replace(frase, ('-'), ' ')
    y = str.replace(x, (','), ' ')
    z = str.replace(y, (':'), ' ')
    w = str.replace(z, (';'), ' ')
    r = str.replace(w, ('.'), ' ')
    s = str.replace(r, ('!'), ' ')
    a = str.replace(s, ('?'), ' ')
    return a

def inverte(texto):
    '''
    string -> string'''
    b = str.lower(retira_pontuacao(texto))
    c = str.split(b)[::-1]
    d = str.join(' ',c)
    return d