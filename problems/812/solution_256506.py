def retira_pontuacao(frase):
    if "."or"," in frase:
        return frase.replace("."," ") and frase.replace(","," ")