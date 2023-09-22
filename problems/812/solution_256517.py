def retira_pontuacao(frase):
    frase1 = frase.replace(","," ")
    frase2 = frase1.replace("-"," ")
    return frase2.replace("."," ")