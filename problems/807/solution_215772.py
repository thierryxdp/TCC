def conta_frases(frases):
    v=str.split(frases,"!")
    x=str.split(frases,".")
    z=str.split(frases,"?")
    y=str.split(frases, int("...")-2)
    
    
    return len(v)-1+len(x)-1+len(z)-1+len(y)-1