def retira_pontuacao(ponto):
    if ponto.endswith("!"):
        x = ponto.replace("!"," ")
        return x
    if ponto.endswith("?"):
        x = ponto.replace("?"," ")
        return x