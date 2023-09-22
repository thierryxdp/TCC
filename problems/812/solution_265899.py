def retira_pontuacao(frase):
    pontuacao=['-',',',':',';','.']
    if pontuacao in frase:
        list.remove(frase, pontuacao)
    return frase