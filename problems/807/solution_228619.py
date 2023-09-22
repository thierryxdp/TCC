def conta_frases(texto):
    a=list.split(texto,".")
    b=list.split(a,"!")
    c=list.split(b,"?")
    d=list.split(c,"...")
    return len(d)