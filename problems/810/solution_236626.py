def inverte(texto):
    '''
    string -> string'''
    b = str.lower(texto)
    c = str.split(b)
    d = str.join(' ',c)
    return d

def retira_pontuacao(inverte):
    '''Funcao que dada uma frase, retira a pontuacao da frase e substitui por espaço.
    string -> string'''
    x = str.replace(inverte, ('-'), ' ')
    y = str.replace(x, (','), ' ')
    z = str.replace(y, (':'), ' ')
    w = str.replace(z, (';'), ' ')
    r = str.replace(w, ('.'), ' ')
    s = str.replace(r, ('!'), ' ')
    a = str.replace(s, ('?'), ' ')
    return a