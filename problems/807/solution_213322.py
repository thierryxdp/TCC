def conta_frases(t):
    "Dado um texto, informa o número de frases nesse texto (str --> int)"""
    T = str.replace(t,"!",".")
    T = str.replace(T,"?",".")
    T = str.replace(T,"...",".")
    T = str.split(T,".")
    return len(T)-1