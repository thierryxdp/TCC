def conta_frases(texto):
    
    i = 0    
    numero_pontos1 = str.count(texto, ".")
    numero_texto = i + 1
    numero_pontos2 = str.count(texto, "?")
    numero_texto = i + 1
    numero_pontos3 = str.count(texto, "!")
    numero_texto = i + 1
    numero_pontos3 = str.count(texto, "...")
    numero_texto = i + 1
    
    return numero_texto