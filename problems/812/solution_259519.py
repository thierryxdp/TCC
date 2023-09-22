def retira_pontuacao(frase):

    f1=frase.replase("-")
    f2=frase.replase(".")
    f3=frase.replase(",")
    f4=frase.replase("!")
    f5=frase.replase("?")
    f6=frase.replase(";")
    f7=frase.replase(".,")
    f8=frase.replase(":")
    f9=frase.replase("...")
    if "..." in frase:
        return f1+f2+f3+f4+f5+f6+f7+f8+f9-(3*f9)
    
    return f1+f2+f3+f4+f5+f6+f7+f8+f9