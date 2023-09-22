def conta_frases(t):
    p=str.count(t, ".")
    e=str.count(t, "!")
    in=str.count(t,"?")
    r=str.count(t, "...")
    if  "..." in t: 
        return (p+e+i-(r*2))
    else:
        return (p+e+i+r)