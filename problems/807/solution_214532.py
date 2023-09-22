def conta_frases(s):
    
    x=str.split(s,".")
    y=str.split(s,"!")
    z=str.split(y,"?")
    return len(z)