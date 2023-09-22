def conta_frases(texto):
    pts = str.split(texto,".")
    exc = list.remove(pts,!)
    ite = list.remove(exc,"?")
    ret = list.remove(ite,"...")
    a = ret
    b = len(a)
    return b