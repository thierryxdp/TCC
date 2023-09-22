def conta_frases (s):
    x = str.partition(s,".")
    y = str.partition(s,"!")
    z = str.partition(s,"?")
    w = str.partition(s,"...")
    if str.endswith(x,"."):
        return len(x,".")
    else:
        return len(x) + len(y) + len(z) + len(w)