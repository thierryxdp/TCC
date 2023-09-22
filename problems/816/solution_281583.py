def maiores(lista,n):
    a = lista.append(n)
    b = lista.sort()
    c = str(lista)
    c1 = str(n)
    d = lista.split(c1)
    d1 = str(d)
    e = d1.replace("', ', ","[").replace("'","").replace("[","",2).replace("]","",1)
    f = e.find("[")
    g = e.find("]")
    h = e[f:g+1]
    return h