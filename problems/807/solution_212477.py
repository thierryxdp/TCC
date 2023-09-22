def conta_frases(x):
    x=str.split(x,".")
    x=str.split(x,"!")
    x=str.split(x,"?")
    x=str.split(x,"...")
    return len(x)