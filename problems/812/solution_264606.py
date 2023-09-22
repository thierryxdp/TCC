def retira_pontuacao(frase):
    ''' '''
    pontuacao=['-',',',':',';','.']
    frase.replace('-'," ")
    frase.replace(','," ")
    frase.replace(':'," ")
    frase.replace(';'," ")
    frase.replace('.'," ")
    return  frase