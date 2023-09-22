def conta_frases(texto):
    return str.replace("...",".")+str.count(texto,"!") + str.count(texto,"?") + str.count(texto,".")