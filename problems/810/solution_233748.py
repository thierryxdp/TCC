def inverte(cadeia):
    """Esta função retira todos os caracteres de pontuação no texto"""
    pontuacao = "!","?",".",",","-"
    for car in pontuacao:
        cadeia = cadeia.replace(car, " ")
    
    x = cadeia.split (" ")
    y = x[::-1]
    z = y.join (" ")
    return  z