def inverte (frase):
    a = frase.replace("-"," ")
    b = a.replace(","," ")
    c = b.replace(":"," ")
    d = c.replace(";"," ")
    e = d.replace("..."," ")
    f = e.replace("."," ")
    g = f.replace("?"," ")
    h = g.replace("!"," ")
    lista = h.split()
    lista2 = lista[::-1]
    frasef = " "
    return frasef.join(lista2)