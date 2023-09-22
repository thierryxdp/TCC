def inverte (frase):
    """ inverte uma frase de entrada 'f', sem letras maiúsculas e sem pontuação """
    a = str.replace(f,"!"," ")
    b = str.replace(a,"?"," ")
    c = str.replace(b,";"," ")
    d = str.replace(c,":"," ")
    e = str.replace(d,"."," ")
    f = str.replace(e,","," ")
    g = str.replace(f,"-"," ")
    h = str.lower (g)
    return h[::-1]