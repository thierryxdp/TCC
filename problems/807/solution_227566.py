def conta_frases(texto):
    list(texto)
    i=0
    n=1
    import string
    p = string.punctuation
    while i<len(texto):
        if texto[i] in p:
            n=n+1
            return n
        i = i + 1