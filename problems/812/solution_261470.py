def retira_pontuacao(frase):
    for char in ".!?,-":
    text = frase.replace(char, "")
    return text