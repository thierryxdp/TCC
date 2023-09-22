def retira_pontuacao(frase):
    f = str.replace(frase, "...", " ")
    f = str.replace(f, "?", " ")
    f = str.replace(f, "!", " ")
    f = str.replace(f, ".", " ")
    f = str.replace(f, ":", " ")
    f = str.replace(f, ":", " ")
    f = str.replace(f, "-", " ")
    f = str.replace(f, ",", " ")
    return f