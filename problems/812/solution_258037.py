def retira_pontuacao(frase):
    pontuacao = "!?.,-" 
    for pontuacao in pontuacao:
        x = frase.resub(pontuacao, ' ')
        return x