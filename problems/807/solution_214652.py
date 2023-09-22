def conta_frases(x):
    y = x.replace("...",",")
    p = y.replace("!",",")
    k = p.replace(".",",")
    t = k.replace("?",",")
    j = str.strip(t)
    u = t.split(",")
    return len(u)