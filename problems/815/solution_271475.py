def insere (lista_numero, n):
    a = str(lista_numero)
    b = a.replace('[','').replace(']','').replace("'","")
    c = b.split(',')
    d = list.append(c, n)
    e = str(c)
    f = e.replace("'","").replace("  "," ").replace('[','').replace(']','')
    g = max(f)
    h = str(g)
    i = h.replace("' '","").replace("' ","'")
    return g