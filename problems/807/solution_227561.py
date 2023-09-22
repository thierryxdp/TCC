def conta_frases(texto):
    n=[]
    import string
    p = string.punctuation
    for p in texto:
        n.append(p)
       
    return len(n)