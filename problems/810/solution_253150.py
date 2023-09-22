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
    
    x = retira_pontuacao(frase).split()
    x.reverse()
    y = ' '.join(x)
    return y