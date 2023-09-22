def conta_frases(frases):
    v=str.split(frases,"!")
    y=str.split(frases,".")
    z=str.split(frases,"?")
    if len(y) = 3:
        return len(v)-1+len(z)-1+len(y)-3