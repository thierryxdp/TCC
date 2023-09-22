def conta_frases(texto):
    """ """
    x = str.find(texto," ")+ str.find(texto,".") + str.find(texto,"?") + str.find(texto,"...")+ str.find(texto,'!')
    return x + 1