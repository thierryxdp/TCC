def retira_pontuacao(frase):
    a = '-'
    b = ','
    c = ':'
    d = ';'
    e = '.'
    f = '!'
    g = '?'
    h = '...'
    lst_carac = [a, b, c, d, e, f, g, h]
    if lst_carac in frase:
        a = frase.replace(lst_carac[:], ' ')
        return a