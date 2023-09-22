def retira_pontuacao(frase):
    
    frase_nova=str.replace(str(frase),frase.punctuation,' ')
    
    return frase_nova