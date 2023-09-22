def retira_pontuacao(frase):
    if "." in frase:
        return str.replace(frase, ".", " ")