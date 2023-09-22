def conta_frases (x):
    y = x.replace("..."," ")
    p = y.replace("!"," ")
    k = p.replace("."," ")
    t = k.replace("?"," ")
    t = str.strip(t)
    t = t.split(" ")
    return len(t)