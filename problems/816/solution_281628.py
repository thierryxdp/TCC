def maiores(lista,n):
    a = lista.append(n)
    b = lista.sort()
    c = str(lista)
    c1 = str(n)
    d = c.split(c1)
    d1 = str(d)
    e = d1.replace("', ', ","[#").replace("['","",2).replace("']","",1)
    f = e.find("[#")
    g = e.find("]")
    h = e[f:g+1]
    if str.count(h,"#")==0:
        return []
    i = h.replace("'","").replace("#","").replace("]","").replace("[","")
    j = i.split(",")
    k = i
    return k