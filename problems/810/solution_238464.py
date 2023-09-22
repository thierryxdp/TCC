def inverte(frase):
    """ """
    a = str.replace(frase,"-"," ")
    b = str.replace(a,"?"," ")
    c = str.replace(b,"!"," ")
    d = str.replace(c,","," ")
    e = str.replace(d,":"," ")
    f = str.replace(e,";"," ")
    g = str.replace(f,"."," ")
    h = str.replace(g,"..."," ")
    
    x = str.lower(h)
    y = str.split(x)
    z = y[::-1]
    return str.join(" ",z)