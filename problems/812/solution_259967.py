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