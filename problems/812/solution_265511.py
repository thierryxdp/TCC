def retira_pontuacao(frase):
    if "." in frase:
        s=str.replace(frase, ".", " ")
    if "," in frase:
        s=str.replace(frase, "," , " ")