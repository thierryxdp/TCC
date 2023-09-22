def retira_pontuacao(frase):
    return str.replace(frase, ",", " ") and str.replace(frase, ".", " ") and str.replace(frase,":", " ") and str.replace(frase, "-", " ") and str.replace(frase, "!", " ")