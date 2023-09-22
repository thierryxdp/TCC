def retira_pontuacao (x):
    y = x.replace("."," ")
    p = y.replace(","," ")
    o = p.replace("!"," ")
    k = o.replace("?"," ")
    d = k.replace(":"," ")
    k2= d.replace(";"," ")
    k3= k2.lstrip(k2)
    return k3