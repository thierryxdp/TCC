def conta_frases(texto):
    
    x=str.split(texto,".")
    y=str.split(str(x),"!")
    z=str.split(y,"?")
    a=str.split(z,"...")
    
    return len(a)