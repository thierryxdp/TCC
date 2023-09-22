def conta_frases(a):
    "."!="..."
    b=str.count(a,"...")
    c=str.count(a,".")
    d=str.count(a,"!")
    e=str.count(a,"?")
    if "..." in a:
        return b+c+d+e-3*b
    return b+c+d+e