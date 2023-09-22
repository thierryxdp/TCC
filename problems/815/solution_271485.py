def insere (lista_numero, n):
    a = str(lista_numero)
    n = n
    a2 = lista_numero.extend(n)
    b = a.replace('[','').replace(']','').replace("'","")
    c = b.split(',')
    d = list.append(c, n)
    e = str(c)
    f = e.replace("'","").replace("  "," ").replace('[','').replace(']','')
    g = max(f)
    return a2