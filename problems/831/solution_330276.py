def lingua_p(g):
    vogais = ["a", "e", "i", "o", "u"]
    for e in range(len(g)):
        if g[e] in vogais:
            g = g[0:e+1] + "p" + g[e:len(g)]
    return g