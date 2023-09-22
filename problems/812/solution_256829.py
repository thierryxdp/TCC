def retira_pontuacao (x):
    y = x.replace("."," ")
    p = y.replace(","," ")
    o = p.replace("!"," ")
    k = o.replace("?"," ")
    d = k.replace(":"," ")
    return d