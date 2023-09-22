def inverte(cadeia):
    """Esta função retira todos os caracteres de pontuação no texto"""
    pontuacao = "!","?",".",",","-"
    for car in pontuacao:
        cadeia = cadeia.replace(car, " ")
    
    x = cadeia.split (" ")
    y = x.str.lower(x)
    return y