def inverte(frase):
    """ dada uma frase retira a pontuaçao,deixa os caracteres minusculo e e retorna o inverso da frase"""
    """str->str"""
    x = frase
    u = str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(x, "-", " "), ",", " "), ":", " "), ";", " "), "!", " "), "?", " "), ".", " ")
    y = str.split(str.lower(u))
    a = list(y)
    a.reverse( )
    c = ' '.join(a)
    return c