def retira_pontuacao(frase):
    "retira pontuacões de uma frase"
    "str  -> str"
    if "-" in frase:
        frase=frase.replace("-"," ")
        return frase
    elif "," in frase:
        frase=frase.replace(","," ")