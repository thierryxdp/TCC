def retira_pontuacao(texto):
    """troca as pontuações da função por espaço"""
    pontuacoes = ("...","!","?",".",",","-")
    for pontuacao in pontuacoes:
        texto = texto.replace(pontuacao," ")
    return texto