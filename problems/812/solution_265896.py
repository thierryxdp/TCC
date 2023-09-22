def retira_pontuacao(frase):
    frase=[frase]
    pontuacao=['-',',',':',';','.']
    for pontuacao in frase:
        list.remove(pontuacao)
    return frase