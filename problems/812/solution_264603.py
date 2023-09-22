def retira_pontuacao(frase):
    ''' '''
    pontuacao=['-',',',':',';','.']
    str.replace(frase,'-'," ")
    str.replace(frase,','," ")
    str.replace(frase,':'," ")
    str.replcae(frase,';'," ")
    str.replace(frase,'.'," ")
    return  frase