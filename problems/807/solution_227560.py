def conta_frases(texto):
    n=[]
    import string
    p = string.punctuation
    for c in p:
        n.append(c)
       
    return len(n)