def retira_pontuacao(frase):
    a = frase.replace('!', ' ')
    b = a.replace('?', ' ')
    c = b.replace('.', ' ')
    d = c.replace(',', ' ')
    e = d.replace(':', ' ')
    f = e.replace(';', ' ')
    g = f.replace('-', ' ')
    return g