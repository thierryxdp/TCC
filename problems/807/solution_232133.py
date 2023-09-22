def conta_frases(texto):
    pts = str.split(texto,".")
    exc = str.split(texto,"!")
    ite = str.split(texto,"?")
    ret = str.split(texto,"...")
    
    a = pts + exc + ite + ret
    b = len(a)
    return b