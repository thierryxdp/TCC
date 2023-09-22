def insere (lista_numero, n):
    a = lista_numero.append(n)
    b = a.replace('[','').replace(']','').replace("'","")
    c = b.split(',')
    d = list.append(c, n)
    e = str(c)
    f = e.replace("'","").replace("  "," ").replace('[','').replace(']','')
    g = max(f)
    return lista_numero