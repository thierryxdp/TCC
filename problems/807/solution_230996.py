def conta_frases(x):
    "."=!"..."
    a=str.count(x,"...")
    b=str.count(x,".")
    c=str.count(x,"!")
    d=str.count(x,"?")
    if"..."in x:
        return a+c+d+b-3*b
    return a+b+c+d