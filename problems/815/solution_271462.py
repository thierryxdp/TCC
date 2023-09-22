def insere (lista_numero, n):
    a = str(lista_numero)
    b = a.replace('[',',').replace(']','').replace("'","")
    c = b.split(',')
    d = list.append(c, n)
    e = str(c)
    f = e.replace("'","").replace("  "," ").replace('[','').replace(']','')
    g = f.split(',')
    h = str(g)
    return h