def retira_pontuacao(frase):
    ''' '''
    pontuacao=['-',',',':',';','.']
    a = str.replace(frase,'-'," ")
    b = str.replace(frase,','," ")
    c = str.replace(frase,':'," ")
    d = str.replcae(frase,';'," ")
    e =  str.replace(frase,'.'," ")
    return  a+b+c+d+e