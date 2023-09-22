def retira_pontuacao(frase):
    "retira pontuacões de uma frase"
    "str  -> str"
    if "," or "-" or "." or ":" or ";" in frase:
        frase=frase.replace(","," ")
        frase=frase.replace("-"," ")
        frase=frase.replace("."," ")
        frase=frase.replace(":"," ")
        frase=frase.replace(";"," ")
        return frase