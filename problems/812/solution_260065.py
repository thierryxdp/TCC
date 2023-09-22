def retira_pontuacao(frase):
    "retira pontuacões de uma frase"
    "str  -> str"
    if "," or "-" in frase:
        frase=frase.replace(","," ")
        frase=frase.replace("-"," ")
        
        return frase