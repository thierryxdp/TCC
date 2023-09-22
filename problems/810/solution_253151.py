def retira_pontuacao(frase):
    '''funcao que retorna uma dada frase sem a sua pntuacao.
    str-->str'''
    a = frase.replace('–', ' ')
    b = a.replace(',', ' ')
    c = b.replace(':', ' ')
    d = c.replace(';', ' ')
    e = d.replace('.', ' ')
    f = e.replace('!', ' ')
    g = f.replace('?', ' ')
    h = g.replace('...', ' ')
    i = h.replace('-', ' ')
    return i

def inverte(frase):
    
    x = frase.lower()
    y = retira_pontuacao(frase).split()
    y.reverse()
    z = ' '.join(y)
    return z