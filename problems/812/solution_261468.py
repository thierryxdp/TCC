def retira_pontuacao(frase):
    for char in ".!?,-":
        text = text.replace(char, "")
    return text