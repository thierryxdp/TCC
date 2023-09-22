def conta_frases(a):
    s=a
    x=a
    y=a
    a=str.split(a,"?")
    s=str.split(s,"!")
    x=str.split(x,".")
    y=str.split(y,"...")
    z=(len(a)-1)+(len(s)-1)+(len(x)-1)+(len(y)-1)
    return z