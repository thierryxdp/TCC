def conta_frases(a):
    a=str.split(a,"?")
    a=str.split(a,".")
    a=str.split(a,"!")
    return len(a)