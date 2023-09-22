def insere (lista_numero, n):
    a = str(lista_numero)
    b = a.replace('[','').replace(']','').replace("'","")
    c = b.split(',')
    c1 = list(n)
    d = list.append(c,c1)
    e = str(c)
    f = e.replace("'","").replace("  "," ").replace('[','').replace(']','').replace(" ","")
    g = f.split(',')
    h = g.sort()
    return c