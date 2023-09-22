def retira_pontuacao(frase):
    
    frase_nova=str.replace(str(frase),str(string.punctuation),' ')
    
    return frase_nova