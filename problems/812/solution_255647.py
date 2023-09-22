def retira_pontuacao(frase):
    """função que retorna uma fn=unção com a pontuação substituida por espaço"""
    """str->str"""
    a = str.replace(frase,'-',' ')
    b = str.replace(a, ',', ' ')
    c = str.replace(b, ':', ' ')
    d = str.replace(c, ';', ' ')
    e = str.replace(d, '.', ' ')
    f = str.replace(e, '?', ' ')
    g = str.replace(f, '!', ' ')
    return g