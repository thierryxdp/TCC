def conta_frases (x):
    y = x.replace("...",";")
    p = y.replace("!",";")
    k = p.replace(".",";")
    t = k.replace("?",";")
    return t