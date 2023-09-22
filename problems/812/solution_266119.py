def retira_pontuacao(frase):
    ls = [("...", " "), (".", " "), ("!", " "), ("?", " "), (",", " "), ("-", " "), (":", " "), (";", " ")]
    for m in ls:
        frase = str.replace(frase, m[0], m[1])
    return frase