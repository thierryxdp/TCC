def retira_pontuação(frase):
    frase= frase.replace ("..."," ").replace("!"," ").replace("?"," ").replace("-"," ")
    return frase