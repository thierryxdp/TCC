def retira_pontuacao (frase):
    ''' '''
    frase1= str.replace(frase,'-',' ')
    frase2= str.replace(frase1,',',' ')
    return str.join(frase2)