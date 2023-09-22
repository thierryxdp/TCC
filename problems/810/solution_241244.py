def retira_pontuacao(texto):
    'Dado um texto troca as pontuaçoes (-/!/,/. etc) por " ". str -> str'
    a = str.replace(texto, ('-'), ' ')
    b = str.replace(a, (','), ' ')
    c = str.replace(b, (':'), ' ')
    d = str.replace(c, (';'), ' ')
    e = str.replace(d, ('.'), ' ')
    f = str.replace(e, ('!'), ' ')
    final = str.replace(f, ('?'), ' ')
    return final
def inverte(texto):
    g = str.lower(retira_pontuacao(texto))
    h = str.split(g)[::-1]
    fim = str.join(' ',h)
    return fim