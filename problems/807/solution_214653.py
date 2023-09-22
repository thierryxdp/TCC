def conta_frases(x):
    y = str.split(x,".")
    o = str.split(y,"...")
    d = str.split(o,"!")
    k = str.split(d,"?")
    return len(k)