def conta_frases(frases):
    v=str.split(frases,"!")
    y=len(str.split(frases,"..."))-2
    z=str.split(frases,"?")
    x=str.split(frases,".")
    
    return len(v)-1+len(z)-1+y+len(x)-1