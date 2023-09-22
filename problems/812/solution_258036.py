def retira_pontuacao(frase):
    pontuacao = "!?.,-" 
    for pontuacao in pontuacao:
        x = frase.replace(pontuacao, ' ')
        print (x)