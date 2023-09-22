def conta_frases(frases):
    v=str.split(frases,"!")
    x=str.split(frases,".")
    y=len(str.split(frases,"..."))-3
    z=str.split(frases,"?")
    
    return len(v)+len(x)+y-1+len(z)-1