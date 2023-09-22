def retira_pontuacao(frase):
    pontuacao=['-',',',':',';','.']
    for pontuacao in frase:
        list.remove(frase, pontuacao)
    return frase