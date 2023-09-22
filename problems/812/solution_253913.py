def retira_pontuação(frase):
    
    frase = str.replace(frase,".", " ")
    frase = str.replace(frase,",", " ")
    frase = str.replace(frase,":", " ")
    frase = str.replace (frase,"-"," ")
    frase = str.replace(frase,";"," ")

    return frase