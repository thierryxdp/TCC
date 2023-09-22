def retira_pontuacao(frase):
    x = str.replace(frase, "...", " ")
    x = str.replace(x, "?", " ")
    x = str.replace(x, "!", " ")
    x = str.replace(x, ".", " ")
    x = str.replace(x, ":", " ")
    x = str.replace(x, ":", " ")
    x = str.replace(x, "-", " ")
    x = str.replace(x, ",", " ")
    return x