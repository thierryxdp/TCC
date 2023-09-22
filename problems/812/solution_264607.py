def retira_pontuacao(frase):
    ''' '''
    pontuacao=['-',',',':',';','.']
    a=frase.replace('-'," ")
    b=frase.replace(','," ")
    c= frase.replace(':'," ")
    d=frase.replace(';'," ")
    e=frase.replace('.'," ")
    return  a+b+c+d+e