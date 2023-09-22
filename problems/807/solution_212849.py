def conta_frases(texto):
    return list(str.replace(str.replace(texto," ",""),".",","))