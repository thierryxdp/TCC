def inverte(frase):
    palavras = str.split(frase)
    list.reverse(palavras)
    espaco = ""
    x = str.lower(str.join(espaco, palavras))
    y = x.replace("."," ")
    p = y.replace(","," ")
    o = p.replace("!"," ")
    k = o.replace("?"," ")
    d = k.replace(":"," ")
    k2 = d.replace("-"," ")
    k3= k2.replace(";"," ")
    return k3