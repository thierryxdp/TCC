def insere (lista_numero, n):
    a = str(lista_numero)
    a1 = n
    a2 = a+a1
    b = a.replace('[','').replace(']','').replace("'","")
    c = b.split(',')
    d = list.append(c, n)
    e = str(c)
    f = e.replace("'","").replace("  "," ").replace('[','').replace(']','')
    g = max(f)
    return a2