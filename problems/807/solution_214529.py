def conta_frases(s):
    x=str.split(s,".")
    y=str.split(x,"!")
    z=str.split(y,"?")
    return len(z)