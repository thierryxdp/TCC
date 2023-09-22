def conta_frases (x):
    " A função recebe um frase "
    " As funções de y a t, pegam os
    y = x.replace("...","*")
    p = y.replace("!","*")
    k = p.replace(".","*")
    t = k.replace("?","*")
    o = str.split(t,"*")
    d = len(o)-1
    return d