def conta_frases(frases):
    v=str.split(frases,"!")
    x=str.split(frases,".")
    y=str.split(frases,"...")
    z=str.split(frases,"?")
    return len(v)-1+len(x)+2+len(y)-4+len(z)-1