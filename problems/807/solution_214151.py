def conta_frases(texto):
    l1=str.count(texto,"!")
    l2=str.count(texto,"?")
    texto=str.replace(texto,"...",".")
    l3=str.count(texto,".")
    return l1+l2+l3