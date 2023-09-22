def retira_pontuacao(texto):
    """Dada um texto retira a pontuacao da mesmo e substitui por espaço.
    str --> str"""
    x = str.replace(texto, ('-'), ' ')
    y = str.replace(x, (','), ' ')
    z = str.replace(y, (':'), ' ')
    w = str.replace(z, (';'), ' ')
    r = str.replace(w, ('.'), ' ')
    s = str.replace(r, ('!'), ' ')
    a = str.replace(s, ('?'), ' ')
    return a
def inverte(texto):
    """Dado um texto inverte a ordem das palavras
    str --> str"""
    b = str.lower(retira_pontuacao(texto))
    c = str.split(b)[::-1]
    d = str.join(' ',c)
    return d