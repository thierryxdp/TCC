def conta_frases(s):
    a=str.count(s,".")
    b=str.count(s,"!")
    c=str.count(s,"?")
    d=str.count(s,"...")
    e=str.split(s)
    if e.endswith("..."):
        return a+b+c+3
    else:
        return a+b+c