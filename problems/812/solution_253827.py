def retira_pontuacao(cadeia):
    """Esta função retira todos os caracteres de pontuação no texto"""
    pontuacao = "!","?",".",",","-"
    for car in pontuacao:
        cadeia = cadeia.replace(car, " ")
    
    return cadeia