def conta_frases (x):
    y = x.replace("...","@")
    p = y.replace("!","@")
    k = p.replace(".","@")
    t = k.replace("?","@")
    t = str.strip(t)
    t = str.split(t,"@")
    return len(t)-1