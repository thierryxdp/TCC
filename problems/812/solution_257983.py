def retira_pontuacao(ponto):
    if ponto.find("!"):
        x = ponto.replace("!"," ")
        return x
    if ponto.find("-"):
        x = ponto.replace("-"," ")
        return x