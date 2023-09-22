def retira_pontuacao1 (frase):
    frese=frase.replace("-"," ")
    frese=frase.replace(","," ")
    frese=frase.replace(":"," ")
    frese=frase.replace(";"," ")
    frese=frase.replace("."," ")
    frese=frase.replace("?"," ")
    frese=frase.replace("!"," ")
    return frase