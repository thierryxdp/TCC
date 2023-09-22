def freq_palavras (s):
    r = {}
    S = str.split (s)
    for e in S:
        r[e] = list.count (S, e)
    return r