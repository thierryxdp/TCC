def conta_frases(texto):
    contador1 = str.count(texto,".")-1
    contador2 = str.count(texto,"...")-1
    contador3 = str.count(texto,"?")-1
    contador4 = str.count(texto,"!")-1

    return contador1+contador2+contador3+contador4