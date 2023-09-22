def retira_pontuacao(frase):
    ''' '''
    pontuacao=['-',',',':',';','.']
    a=frase.replace(pontuacao," ")
    return a