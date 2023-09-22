def conta_frases(cadeia):
    pontuacao = "!","?",".",",","-",":",";"
    for car in pontuacao:
        cadeia = cadeia.replace(car, " ")
    
    x = cadeia.split (" ")
    return len(x)