def retira_pontuacao(frase):
    frase=str
    pontuacao=['-',',',':',';','.']
    if pontuacao in frase:
        list.remove(frase, pontuacao)
    return frase