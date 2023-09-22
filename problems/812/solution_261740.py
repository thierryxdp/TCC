def retira_pontuacao(frase):
    """Retorna a frase de entrada invertida; str->str"""
    a = str.replace(frase, '.', ' ')
    b = str.replace(a, '!', ' ')
    c = str.replace(b, '?',' ')
    d = str.replace(c, '...',' ')
    e = str.replace(d, '-', ' ')
    f = str.replace(e, ',', ' ')
    g = str.replace(f, ':', ' ')
    frase = g
    return frase