def retira_pontuacao(frase):
    if "."or","or";"or":" in frase:
        return frase.replace("."," ") and frase.replace(","," ")