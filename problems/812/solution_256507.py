def retira_pontuacao(frase):
    if "."and"," in frase:
        return frase.replace("."," ") and frase.replace(","," ")