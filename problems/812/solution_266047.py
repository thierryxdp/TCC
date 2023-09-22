def retira_pontuacao(frase):
    a=frase.replace(","," ")
    b=frase.replace("."," ")
    c=frase.replace("-"," ")
    return a and b and c