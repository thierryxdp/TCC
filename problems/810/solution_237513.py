def inverte(frase):
    """
    str -> str"""
    a=str.replace (frase,","," ")
    b=str.replace(a,"."," ")
    c=str.replace(b,"!"," ")
    d=str.replace(c,"?"," ")
    e=str.replace(d,"-"," ")
    f=str.replace(e,":"," ")
    g=str.replace(f,";"," ")
    h=str.lower(g)
    i=str.split(h)[::-1]
    return str.join(i,[::-1])