def retira_pontuacao(frase):
    pontuacao = "!?.,-" 
    for pontuacao in pontuacao:
        frase = frase.replace(pontuacao, '')
        print(frase)