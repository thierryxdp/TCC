def freq_palavras(x):
    palavras = x.split()
    chaves = {}
    for y in palavras:
        l = palavras.count(y)
        if y not in chaves:
            chaves[y] = l
    return chaves