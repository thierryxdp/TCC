def retira_pontuacao(frase):

    f1=frase.replase("-")
    f2=frase.replase(",")
    f3=frase.replase(":")
    f4=frase.replase(";")
    f5=frase.replase("?")
    f6=frase.replase(".")
    
    return f1+f2+f3+f4+f5+f6