def freq_palavras(frases):
    a = frases.split()
    import collections
    b = dict(collections.Counter(a))
    return b