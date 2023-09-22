def maiores(lista,n):
    a = lista.append(n)
    b = lista.sort()
    c = str(lista)
    c1 = str(n)
    d = c.split(c1)
    d1 = str(d)
    e = d1.replace("', ', ","[").replace("'","").replace("[","",2)
    return e