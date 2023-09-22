def conta_frases(s):
    x = str.split(s,",","...","!","?")
    return len(x)