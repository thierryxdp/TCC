def inverte (frase):
    """ inverte uma frase de entrada 'f', sem letras maiúsculas e sem pontuação """
    a = str.replace(frase,"!"," ")
    b = str.replace(a,"?"," ")
    c = str.replace(b,";"," ")
    d = str.replace(c,":"," ")
    e = str.replace(d,"."," ")
    f = str.replace(e,","," ")
    g = str.replace(f,"-"," ")
    h = str.split (g)
    i = str.lower (h)
    j = i[::-1]
    k = str.join (j," ")
    return k