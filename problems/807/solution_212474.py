def conta_frases(x):
    a=str.split(x,".")
    b=str.split(a,"!")
    c=str.split(b,"?")
    d=str.split(c,"...")
    return len(d)