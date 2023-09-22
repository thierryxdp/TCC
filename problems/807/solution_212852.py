def conta_frases(texto):
    return tuple(str.replace(str.replace(texto," ",""),".",","))