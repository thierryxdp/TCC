def conta_frases(texto):
    texto = str.replace(texto,"?",".")
    texto = str.replace(texto,"!",".")
    texto = str.replace(texto,"...",".")
    
    numeroFrases = str.count(texto,".")
    
    return numeroFrases