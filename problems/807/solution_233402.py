def conta_frases (x):
    i=0
    d=[".","...","!","?"]
    for e in x:
        if e in d:
            return i==i+1
        else:
            return i