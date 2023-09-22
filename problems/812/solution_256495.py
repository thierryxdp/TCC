def retira_pontuacao(frase):
    if "." in frase:
        return frase.replace("."," ")
    if "," in frase:
        return frase.replace(","," ")