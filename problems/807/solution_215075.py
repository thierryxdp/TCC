def conta_frase(oração):
    x = oração
    return str.count(x, "!") + str.count(x,".") + str.count(x,"?")