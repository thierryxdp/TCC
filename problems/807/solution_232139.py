def conta_frases(texto):
    pts = str.split(texto,".")
    text1 = " ".join(pts)
    exc = str.split(text1,"!")
    text2 = " ".join(exc)
    ite = str.split(text2,"?")
    text3 = " ".join(ite)
    ret = str.split(text3,"...")
    a = ret
    b = len(a)
    return b