def retira_pontuacao(frase):
    ''' '''
    pontuacao=['-',',',':',';','.']
    a=frase.replace('-'," ") and frase.replace(','," ") and  frase.replace(':'," ") and frase.replace(';'," ") and frase.replace('.'," ")
    return a