def conta_frases (s):
    x = str.partition(s,".")
    y = str.partition(s,"!")
    z = str.partition(s,"?")
    w = str.partition(s,"...")
    return len(x),len(y)