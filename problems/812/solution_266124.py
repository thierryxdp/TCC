def retira_pontuacao(frase):
    y=str.replace(frase, "...", " ")
    y=str.replace(y, "?", " ")
    y=str.replace(y, "!", " ")
    y=str.replace(y, ".", " ")
    y=str.replace(y, ":", " ")
    y=str.replace(y, ":", " ")
    y=str.replace(y, "-", " ")
    y=str.replace(y, " ", " ")
    return y