def retira_pontuacao(f):
    """A função acima retorna a str f com todas as suas pontuações substituidas por espaço.
       str -> str"""
    f = str.replace(f, '-', ' ')
    f = str.replace(f, ',', ' ')
    f = str.replace(f, ':', ' ')
    f = str.replace(f, ';', ' ')
    f = str.replace(f, '.', ' ')
    f = str.replace(f, '!', ' ')
    f = str.replace(f, '?', ' ')
    f = str.replace(f, '...', ' ')
    return f
def inverte(f):
    """"""
    rp = retira_pontuacao(f)
    l = str.split(rp)
    i = l[::-1]
    s = str.join(' ', i)
    return s