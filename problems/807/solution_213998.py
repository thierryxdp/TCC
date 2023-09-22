def conta_frases(texto):
    return str.replace("...",".",-1)+str.count(texto,"!") + str.count(texto,"?") + str.count(texto,".")