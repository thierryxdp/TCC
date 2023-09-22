def retira_pontuacao(frase):
    a = '-'
    b = ','
    c = ':'
    d = ';'
    e = '.'
    f = '!'
    g = '?'
    h = '...'
    'A' = [a, b, c, d, e, f, g, h]
    if 'A' in frase:
        a = frase.replace('A', ' ')
        return a