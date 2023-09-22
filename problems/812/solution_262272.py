def retira_pontuacao(frase):
    
    frase_nova=str.replace(str(frase),str(frase.punctuation),' ')
    
    return frase_nova