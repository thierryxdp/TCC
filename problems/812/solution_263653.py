def retira_pontuacao(frase):
    
    frase2=frase
    str.replace(frase,'-',' ')
    str.replace(frase,',',' ')
    str.replace(frase,':',' ')
    str.replace(frase,'.',' ')
    str.replace(frase,',',' ')
    
    return frase2