def freq_palavras(frases):
    f = frases.split()
    dic = {}
    'p = palavra'
    def rep(f,p):
        q = 0
        for x in f:
            if x == p:
                q = q + 1
        return q
    for p in f:
        dic[p]=rep(f,p)
    return dic