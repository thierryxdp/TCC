def lingua_p(g):
    vogais = ["a", "e", "i", "o", "u", "ú", "é", "ã", "õ", "í"]
    e = 0
    while e < (len(g)):
        if g[e] in vogais:
            g = g[0:e+1] + "p" + g[e:len(g)]
            e = e + 2
        e = e + 1
    return g