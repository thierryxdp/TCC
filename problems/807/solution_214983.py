def conta_frases(s):
    x = str.split(s,",","...","!","?")
    return int(len(x))