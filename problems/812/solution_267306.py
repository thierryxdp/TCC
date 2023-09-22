def retira_frase(frase):
    texto = texto.replace("!",".").replace("?",".").replace("...",".")
    frases = texto.split(" ")
    return len(frase)