def retira_pontuacao(frase):
    frase=[frase]
    pontuacao=['-',',',':',';','.']
    for pontuacao in frase:
        list.remove(frase, pontuacao)
    return frase