def conta_frases(texto):
    
    x=texto.split(,".")
    y=x.split(,"!")
    z=y.split(,"?")
    a=z.split(,"...")
    
    return len(a)