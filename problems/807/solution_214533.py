def conta_frases(s):
    
    x=str.split(s,".")
    y=str.split(s,"!")
    z=str.split(s,"?")
    return len(z)+len(y)+len(x)