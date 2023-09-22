def retira_pontuacao(frase):
    frase.replace(","," ")
    frase.replace("."," ")
    frase.replace(":"," ")
    frase.replace(";"," ")
    frase.replace("–"," ")
    return frase