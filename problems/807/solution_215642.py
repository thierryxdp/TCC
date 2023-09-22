def conta_frases(frases):
    v=str.split(frases,"!")
    x=str.split(frases,".")
    y=str.split(frases,"...")
    z=str.split(frases,"?")
    if len(y)>3:
        return len(v)-1+len(x)-1+len(y)-4+len(z)-1
    else:
        return len(v)-1+len(x)-1+len(y)-1+len(z)-1