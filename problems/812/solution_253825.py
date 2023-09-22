def retira_pontuacao(cadeia):
    pontuacao = "!","?",".",",""-"
    for car in pontuacao:
        cadeia = cadeia.replace(car, " ")
    
    return cadeia