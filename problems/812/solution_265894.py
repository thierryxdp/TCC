def retira_pontuacao(frase):
    frase=[]
    pontuacao=['-',',',':',';','.']
    for pontuacao in frase:
        list.remove(pontuacao)
   return frase