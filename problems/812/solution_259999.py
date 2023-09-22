def retira_pontuacao (frase):
    frese=frase.replace("-"," ")
    frese=frase.replace(","," ")
    frese=frase.replace(":"," ")
    frese=frase.replace(";"," ")
    frese=frase.replace("."," ")
    frese=frase.replace("?"," ")
    frese=frase.replace("!"," ")
    return frase