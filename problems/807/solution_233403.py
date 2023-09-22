def tupla(x):
    d=[]
    d.append(x)
    return d


def conta_frases (x):
    i=0
    d=[".","...","!","?"]
    t=tupla(x)
    for e in t:
        if e in d:
            return i==i+1
        else:
            return i