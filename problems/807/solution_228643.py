def conta_frases(texto):
    a = str.join('#', str.split(texto, '...'))
    c = str.join('#', str.split(a, '?'))
    d = str.join('#', str.split(c, '!'))
    e=str.join('#',str.split(d,'.'))
    print(e)
    lista=e.split("#")
    print(lista)
    numero=len(d.split("#"))
    return numero