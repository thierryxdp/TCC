def retira_pontuacao(frase):
    pontuacao=['...','.','!','?','-',',',':',';']
    for x in pontuacao:
        frase=frase.replace(x,' ')
    return frase