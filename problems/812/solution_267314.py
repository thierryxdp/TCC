def retira_pontuacao(frase):
    texto = texto.replace("-",":").replace(";".").replace(";":".")
    frases = texto.split(". ")
    return len(frase)