def retira_pontuacao(x):
    '''função recebe uma frase de entrada e retorna a frase sem a pontuação.
    string -> string'''
    y = x.replace(',', '')
    a = y.replace('.', '')
    b = a.replace('!', '')
    c = b.replace('?', '')
    d = c.replace('-', '')
    e = d.replace(';', '')
    f = e.replace(':', '')
    return f