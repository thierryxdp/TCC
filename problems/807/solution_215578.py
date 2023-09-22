def conta_frases(frases):
    v=str.split(frases,"!")
    y=str.split(frases,".")
    z=str.split(frases,"?")
    
    return len(v)+len(z)+len(y)