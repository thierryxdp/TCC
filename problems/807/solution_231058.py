def conta_frases(x):
    A = str.split(x,".")
    A = str.split(x,"?")
    A = str.split(x,"...")
    A = str.split(x,"!")
    return len(A)