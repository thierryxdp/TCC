def conta_frases(frases):
    v=str.split(frases,"!")
    x=str.split(frases,".")
    y=str.split(frases,"...")
    z=str.split(frases,"?")
    return len(v)+len(x)+len(y)+len(z)