def conta_frases(frases):
    v=str.find(frases,"!")
    x=str.find(frases,".")
    z=str.find(frases,"?")
    
    return len(v)-1+len(x)-1+len(z)-1