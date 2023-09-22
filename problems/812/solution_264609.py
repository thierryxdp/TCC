def retira_pontuacao(frase):
    ''' '''
    pontuacao=['-',',',':',';','.']
    a=frase.replace('-'," ") or frase.replace(','," ") or frase.replace(':'," ") or frase.replace(';'," ") or frase.replace('.'," ")
    return a