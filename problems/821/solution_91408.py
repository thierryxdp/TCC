def fatorial (n):
    fatores = list (range (n+1))
    list.remove (fatores, 0)
    i = 0
    r = 1
    while i < len(fatores):
        r = r * fatores[i]
        i+= 1
    return r