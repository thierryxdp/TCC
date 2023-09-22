def retira_pontuacao(frase):
    for pontuacao in "!--,:;.?":
        frase = frase.replace(pontuacao, " ")
    return frase