def retira_pontuacao(frases):
    a = frases.replace('–', ' ')
    b = a.replace(',', ' ')
    c = b.replace(':', ' ')
    d = c.replace(';', ' ')
    e = d.replace('!', ' ')
    f = e.replace('?', ' ')
    g = f.replace('...', ' ')
    h = g.replace('.', ' ')
    i = h.replace('-', ' ')
    return i