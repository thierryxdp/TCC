def conta_frases(texto):
    
    x=str.count(texto,".")
    y=str.count(texto,"!")
    z=str.count(texto,"?")
    
    return z+y+x