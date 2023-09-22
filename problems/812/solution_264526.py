def retira_pontuacao(frase):
    '''docs'''
    
    a = frase
    
    b = a.replace(',', ' ')
    c = b.replace('.', ' ')
    d = c.replace('!', ' ')
    e = d.replace('-', ' ')
    f = e.replace(':', ' ')
    g = f.replace(';', ' ')
    
    return g