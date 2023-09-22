def retira_pontuacao(string):
    '''Substitui todos os caracteres de pontuação
       ('—', ',', ':', ';', '.', '!', '?', '...')
       de uma frase por espaço;
       str -> str'''
    a = string.replace('—', ' ')
    b = a.replace(', ', ' ')
    c = b.replace(': ', ' ')
    d = c.replace('; ', ' ')
    e = d.replace('... ', ' ')
    f = e.replace('! ', ' ')
    g = f.replace('? ', ' ')
    h = g.replace('. ', ' ')
    i = h.replace('.', ' ')
    j = i.replace('!', ' ')
    k = j.replace('?', ' ')
    l = k.replace('-', ' ')
    return l