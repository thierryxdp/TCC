def conta_frases (x):
    i=0
    d=[".","...","!","?"]
    for e in x:
        if e in d:
            i=i+1
        else:
            i=i
    return i