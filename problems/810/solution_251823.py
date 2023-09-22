def retira_pontuacao(string):
    a = str.replace(string, '.', '')
    b = str.replace(a, ',', '')
    c = str.replace(b, '-', '')
    d = str.replace(c, ':', '')
    e = str.replace(d, ';', '')
    f = str.replace(e, '?', '')
    g = str.replace(f, '!', '')
    return g

def inverte(string):
    '''inverte a frase dada de traz para frente'''
    new_string = retira_pontuacao(str.lower(string))
    final = str(list.reverse(str.split(new_string)))
    return str.replace(str.replace(final, '[', ''), ']', '')