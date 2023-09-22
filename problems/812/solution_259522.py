def retira_pontuacao(frase):

    f1=frase.replace("-", " ")
    f2=frase.replace(",", " ")
    f3=frase.replace(":", " ")
    f4=frase.replace(";", " ")
    f5=frase.replace("?", " ")
    f6=frase.replace(".", " ")
    
    return f1+f2+f3+f4+f5+f6