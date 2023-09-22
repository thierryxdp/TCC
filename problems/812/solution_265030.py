def retira_pontuacao (frase):
    ''' '''
    frase1= str.replace(frase,'-',' ')
    frase2= str.replace(frase,',',' ')
    return str.join(frase1,frase2)