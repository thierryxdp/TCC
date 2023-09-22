def retira_pontuacao(frase):
    pontuacao = ['.', ';', ':', '?', '!', '-', ',','...']
    for i in range(len(pontuacao)):
        frase = frase.replace(pontuacao[i], " ")
    return frase