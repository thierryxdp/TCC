def conta_frases(string):
    espec = [".","?","...","!"]
    c = [string.count(i) for i in espec]
    c[3] -= c[2] * 3
    j = sum(c)
    return j