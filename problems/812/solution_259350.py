def retira_pontuacao(frase):
    pontuacao = ['!','.',',','-']
    resposta = filter(frase,pontuacao)
    return resposta