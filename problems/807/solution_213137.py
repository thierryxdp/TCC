def conta_frases(texto):
    ''' funcao que dado um texto conta quantas frases o mesmo possui
    str->int'''
    t=texto
    a=texto.strip(t,'.')
    b=a.strip(a,'!')
    return b