def retira_pontuacao(frase):
    chars = "-?!.,"
    for c in chars:
        frase = frase.replace(c, "\\" + c)
        return(frase)