def retira_pontuacao(frase):
    "retira todos os tipos de pontuação em uma frase, str->str"
    frase=str.replace(frase,".", " ")
    frase=str.replace(frase,",", " ")
    frase=str.replace(frase,"-", " ")
    frase=str.replace(frase,"?", " ")
    frase=str.replace(frase,"!", " ")
    frase=str.replace(frase,":", " ")
    frase=str.replace(frase,";", " ")
    frase=str.replace(frase,"...", " ")
    return frase