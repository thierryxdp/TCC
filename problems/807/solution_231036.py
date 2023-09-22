def conta_frases(x):
    A = str.split(x,".")
    B = str.split(x,"?")
    C = str.split(x,"...")
    D = str.split(x,"!")
    return len(D)