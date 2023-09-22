def conta_frases(frases):
    v=str.split(frases,"!")
    x=str.split(frases,"...")
    y=str.split(frases,".")
    z=str.split(frases,"?")
    return len(v)-1+(len(x)/3)+len(y)-1+len(z)-1