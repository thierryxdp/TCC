def substitui (x):
    d=x.replace("...",".")
    return d

def conta_frases (x):
    i=0
    d=[".","...","!","?"]
    t=substitui(x)
    for e in t:
        if e in d:
            i=i+1
        else:
            i=i
    return i